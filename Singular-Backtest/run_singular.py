#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Singular-Backtest — Book Signal Review.

Kural: secilen kapsamda (varsayilan: kural ailesi = family) ayni coinde ayni
anda en fazla bir acik islem. Onceki islem kapanmadan gelen yeni giris sinyali
bloke edilir.

Book Signal motoru her kural (sid) icin filtre basina zaten tek pozisyon
tutar; bu yuzden spec basina tekil kural normal sonucla birebir aynidir.
Anlamli tekillik, ayni ailenin farkli kurallari/zaman dilimleri ayni coinde
ust uste pozisyon actiginda ortaya cikar (varsayilan: family).

Normal metrikler `backtest/filter_layer/dashboard_data.json` sonuclarindan
birebir alinir; singular metrikler islem duzeyindeki parquet kayitlarindan
yeniden hesaplanir.

Kullanim:
  python Singular-Backtest/run_singular.py
  python Singular-Backtest/run_singular.py --scope=portfolio
  python Singular-Backtest/run_singular.py --scope=spec --symbols=20
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone, timedelta

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DASH = os.path.join(ROOT, "backtest", "filter_layer", "dashboard_data.json")
TRADES = os.path.join(ROOT, "backtest", "filter_layer", "results", "trades")
OUT = os.path.join(HERE, "results")

DAY0 = 0  # dashboard daily serileri epoch gunu kullanir
STAKE = 10.0
Y26 = 1767225600000  # 2026-01-01 00:00 UTC
TF_ORDER = {"1h": 0, "4h": 1, "1d": 2, "1w": 3}

SCOPE_LABEL = {
    "family": "Kural ailesi (family), tum spec ve TF'ler birlikte",
    "portfolio": "Tum book portfoyu: coin basina tek acik islem",
    "spec": "Tek kural (sid) — motor zaten tek pozisyon tutar, normal ile ayni",
}


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scope", choices=["family", "portfolio", "spec"], default="family")
    ap.add_argument("--symbols", type=int, default=0, help="ilk N sembol (test)")
    ap.add_argument("--out", default=OUT)
    return ap.parse_args()


def fnum(v, default=0.0):
    try:
        x = float(v)
        return x if math.isfinite(x) else default
    except Exception:
        return default


def period_counts(days):
    """Epoch gunu -> net sozlugunden gun/hafta/ay kâr ve zarar sayilari.

    Hafta Pazartesi 00:00 UTC baslangicli, ay takvim ayidir. Net sifir olan
    donemler sayilmaz.
    """
    daily = defaultdict(float)
    weekly = defaultdict(float)
    monthly = defaultdict(float)
    for day, net in days.items():
        day = int(day)
        daily[day] += net
        dt = datetime.fromtimestamp(day * 86400, tz=timezone.utc)
        week = (dt - timedelta(days=dt.weekday())).date()
        weekly[week] += net
        monthly[(dt.year, dt.month)] += net

    def counts(values):
        return (sum(1 for v in values if v > 0), sum(1 for v in values if v < 0))

    pd_, ld_ = counts(daily.values())
    pw, lw = counts(weekly.values())
    pm, lm = counts(monthly.values())
    return {
        "profitDays": pd_, "lossDays": ld_,
        "profitWeeks": pw, "lossWeeks": lw,
        "profitMonths": pm, "lossMonths": lm,
    }


def metric_from_result(r):
    """dashboard_data results satirindan normal metrikler."""
    n = int(r["n"])
    wins = int(r.get("wins_total") or 0)
    losses = int(r.get("losses_total") or max(0, n - wins))
    total_net = fnum(r.get("total_net"))
    win_hold_h = fnum(r.get("win_hold_h"))
    daily = r.get("daily") or []
    days = defaultdict(float)
    cum, peak, dd = 0.0, 0.0, 0.0
    for row in daily:
        day = int(row[0])
        net = fnum(row[4])
        days[day] += net
        cash = net * STAKE
        cum += cash
        if cum > peak:
            peak = cum
        d = cum - peak
        if d < dd:
            dd = d
    pc = period_counts(days)
    return {
        "trades": n,
        "wins": wins,
        "losses": losses,
        "winRate": wins / n if n else 0.0,
        "retAll": fnum(r.get("avg_net")) * 100.0,
        "ret2026": fnum(r.get("ret_2026")) * 100.0,
        "winRatio": wins / losses if losses else wins,
        "winHoldH": win_hold_h,
        "holdH": fnum(r.get("avg_hold_days")) * 24.0,
        "profitDays": pc["profitDays"],
        "lossDays": pc["lossDays"],
        "profitWeeks": pc["profitWeeks"],
        "lossWeeks": pc["lossWeeks"],
        "profitMonths": pc["profitMonths"],
        "lossMonths": pc["lossMonths"],
        "maxDD": dd,
        "kasaAll": total_net * STAKE,
        "sumR": total_net,
        "pf": fnum(r.get("profit_factor")),
    }


def empty_acc():
    return {
        "n": 0, "wins": 0, "sum": 0.0, "pos": 0.0, "neg": 0.0,
        "durWin": 0.0, "durSum": 0.0, "y26sum": 0.0, "y26n": 0,
        "days": defaultdict(float),
    }


def acc_add(a, net, dur_ms, exit_ms):
    a["n"] += 1
    a["sum"] += net
    if net > 0:
        a["wins"] += 1
        a["pos"] += net
        a["durWin"] += dur_ms
    else:
        a["neg"] += -net
    a["durSum"] += dur_ms
    if exit_ms >= Y26:
        a["y26sum"] += net
        a["y26n"] += 1
    a["days"][int(exit_ms // 86400000)] += net


def acc_metrics(a):
    n = a["n"]
    wins = a["wins"]
    losses = n - wins
    pc = period_counts(a["days"])
    cum, peak, dd = 0.0, 0.0, 0.0
    for day in sorted(a["days"]):
        net = a["days"][day] * STAKE
        cum += net
        if peak < cum:
            peak = cum
        d = cum - peak
        if d < dd:
            dd = d
    return {
        "trades": n,
        "wins": wins,
        "losses": losses,
        "winRate": wins / n if n else 0.0,
        "retAll": (a["sum"] / n * 100.0) if n else 0.0,
        "ret2026": (a["y26sum"] / a["y26n"] * 100.0) if a["y26n"] else 0.0,
        "winRatio": (wins / losses) if losses else wins,
        "winHoldH": (a["durWin"] / wins / 3600000.0) if wins else 0.0,
        "holdH": (a["durSum"] / n / 3600000.0) if n else 0.0,
        "profitDays": pc["profitDays"],
        "lossDays": pc["lossDays"],
        "profitWeeks": pc["profitWeeks"],
        "lossWeeks": pc["lossWeeks"],
        "profitMonths": pc["profitMonths"],
        "lossMonths": pc["lossMonths"],
        "maxDD": dd,
        "kasaAll": a["sum"] * STAKE,
        "sumR": a["sum"],
        "pf": (a["pos"] / a["neg"]) if a["neg"] > 1e-12 else (99.0 if a["pos"] > 0 else 0.0),
    }


def merge_results_normal(rows):
    """Birden cok dashboard result satirini tek normal metrige birlestir."""
    n = wins = losses = 0
    total = 0.0
    y26s = 0.0
    y26n = 0
    durWin = 0.0
    durSum = 0.0
    days = defaultdict(float)
    pos = neg = 0.0
    for r in rows:
        m = metric_from_result(r)
        n += m["trades"]
        wins += m["wins"]
        losses += m["losses"]
        total += m["sumR"]
        pos += fnum(r.get("pos_sum"))
        neg += -fnum(r.get("neg_sum"))
        if m["trades"]:
            y26n += int(r.get("ret_2026_n") or 0)
            y26s += fnum(r.get("ret_2026")) * int(r.get("ret_2026_n") or 0)
            durWin += m["winHoldH"] * 3600000.0 * m["wins"]
            durSum += fnum(r.get("avg_hold_days")) * 24.0 * 3600000.0 * m["trades"]
        for row in (r.get("daily") or []):
            days[int(row[0])] += fnum(row[4])
    pc = period_counts(days)
    cum, peak, dd = 0.0, 0.0, 0.0
    for day in sorted(days):
        net = days[day] * STAKE
        cum += net
        if cum > peak:
            peak = cum
        d = cum - peak
        if d < dd:
            dd = d
    return {
        "trades": n,
        "wins": wins,
        "losses": losses,
        "winRate": wins / n if n else 0.0,
        "retAll": (total / n * 100.0) if n else 0.0,
        "ret2026": (y26s / y26n * 100.0) if y26n else 0.0,
        "winRatio": (wins / losses) if losses else wins,
        "winHoldH": (durWin / wins / 3600000.0) if wins else 0.0,
        "holdH": (durSum / n / 3600000.0) if n else 0.0,
        "profitDays": pc["profitDays"],
        "lossDays": pc["lossDays"],
        "profitWeeks": pc["profitWeeks"],
        "lossWeeks": pc["lossWeeks"],
        "profitMonths": pc["profitMonths"],
        "lossMonths": pc["lossMonths"],
        "maxDD": dd,
        "kasaAll": total * STAKE,
        "sumR": total,
        "pf": (pos / neg) if neg > 1e-12 else (99.0 if pos > 0 else 0.0),
    }


def main():
    args = parse_args()
    t0 = time.time()
    os.makedirs(args.out, exist_ok=True)

    with open(DASH, encoding="utf-8") as f:
        dash = json.load(f)
    specs = dash["specs"]
    spec_by_sid = {s["sid"]: s for s in specs}
    filters = dash["filters"]  # 14
    results = dash["results"]

    # filter_id -> (bit, key, label)
    streams = [("baseline", 15, "baseline", "Filtresiz")]
    for i, f in enumerate(filters):
        streams.append((str(i), i, f["id"], f.get("label_tr") or f.get("label") or f["id"]))

    def scope_key(sid):
        if args.scope == "family":
            return spec_by_sid[sid]["family"]
        if args.scope == "portfolio":
            return "BOOK"
        return sid

    # ------------------------- normal (dashboard'dan) -------------------------
    normal_by_row = {}
    for r in results:
        fid = str(r["filter_id"])
        normal_by_row[(r["sid"], fid)] = metric_from_result(r)

    normal_spec = {}
    for s in specs:
        r = next((x for x in results if x["sid"] == s["sid"] and str(x["filter_id"]) == "baseline"), None)
        normal_spec[s["sid"]] = metric_from_result(r) if r else None

    # aile / filtre / toplam normal
    normal_scope_filter = defaultdict(list)
    normal_filter = defaultdict(list)
    for r in results:
        fid = str(r["filter_id"])
        normal_scope_filter[(scope_key(r["sid"]), fid)].append(r)
        normal_filter[fid].append(r)
    normal_scope_filter = {k: merge_results_normal(v) for k, v in normal_scope_filter.items()}
    normal_filter = {k: merge_results_normal(v) for k, v in normal_filter.items()}
    normal_totals = normal_filter["baseline"]

    # ------------------------------ singular ------------------------------
    sing_row = defaultdict(empty_acc)       # (sid, filter_id)
    sing_scope_filter = defaultdict(empty_acc)  # (scope_key, filter_id)
    sing_filter = defaultdict(empty_acc)    # filter_id
    sing_coin = defaultdict(empty_acc)      # (sid, symbol, 'base')
    blocked_row = defaultdict(int)
    blocked_scope_filter = defaultdict(int)
    blocked_filter = defaultdict(int)
    overlap_violations = 0
    parquet_counts = defaultdict(int)
    parquet_base_counts = defaultdict(int)
    normal_days = defaultdict(lambda: defaultdict(float))
    coin_norm = defaultdict(lambda: [0, 0.0, 0])  # (sid, sym) -> [n, sumR, wins]
    files = sorted(glob.glob(os.path.join(TRADES, "*.parquet")))
    if args.symbols:
        files = files[: args.symbols]
    symbols = [os.path.basename(p)[:-8] for p in files]
    fam_map = {sid: scope_key(sid) for sid in spec_by_sid}
    tfo_map = {sid: TF_ORDER.get(spec_by_sid[sid]["tf"], 9) for sid in spec_by_sid}
    print(f"[book] {len(files)} sembol, kapsam={args.scope}, filtre={len(streams)}")

    for fi, path in enumerate(files):
        sym = os.path.basename(path)[:-8]
        df = pd.read_parquet(path, columns=["sid", "symbol", "side", "entry_time", "exit_time", "net", "accepted_mask"])
        if df.empty:
            continue
        mask = np.asarray(df["accepted_mask"], dtype=np.int64)
        df = df.assign(fam=df["sid"].map(fam_map), tfo=df["sid"].map(tfo_map))
        for fid, bit, _key, _label in streams:
            sel = ((mask >> bit) & 1) == 1
            if not sel.any():
                continue
            g = df[sel]
            # normal sayim dogrulamasi icin parquet adetleri
            for sid, c in g.groupby("sid").size().items():
                parquet_counts[(sid, fid)] += int(c)
                if fid == "baseline":
                    parquet_base_counts[(sid, sym)] += int(c)

            # normal gunluk netler (hafta/ay sayilari icin), sembol bazinda
            gd = g.assign(_day=(g["exit_time"].to_numpy(np.int64) // 86400000))
            for (sid, day), net in gd.groupby(["sid", "_day"], sort=False)["net"].sum().items():
                normal_days[(sid, fid)][int(day)] += float(net)

            # kapsam bazinda (aile / portfoy / spec) tekillik
            for skey, h in g.groupby("fam"):
                h = h.sort_values(["entry_time", "tfo", "side", "sid"], ascending=[True, True, False, True], kind="stable")
                last_exit = -1
                for et, xt, sid, side, net in zip(
                    h["entry_time"].values, h["exit_time"].values, h["sid"].values,
                    h["side"].values, h["net"].values,
                ):
                    if et < last_exit:
                        blocked_row[(sid, fid)] += 1
                        blocked_scope_filter[(skey, fid)] += 1
                        blocked_filter[fid] += 1
                        continue
                    last_exit = int(xt)
                    dm = max(0, int(xt) - int(et))
                    acc_add(sing_row[(sid, fid)], float(net), dm, int(xt))
                    acc_add(sing_scope_filter[(skey, fid)], float(net), dm, int(xt))
                    acc_add(sing_filter[fid], float(net), dm, int(xt))
                    if fid == "baseline":
                        acc_add(sing_coin[(sid, sym, "base")], float(net), dm, int(xt))
                        cn = coin_norm[(sid, sym)]
                        cn[0] += 1
                        cn[1] += float(net)
                        if net > 0:
                            cn[2] += 1

        if (fi + 1) % 25 == 0 or fi == len(files) - 1:
            print(f"  {fi + 1}/{len(files)} sembol - {time.time() - t0:.0f}s")

    # ------------------------------ satirlar ------------------------------
    rows = []
    for r in results:
        sid = r["sid"]
        fid = str(r["filter_id"])
        meta = spec_by_sid[sid]
        nm = normal_by_row[(sid, fid)]
        sm = acc_metrics(sing_row[(sid, fid)])
        blocked = blocked_row[(sid, fid)]
        row = {
            "sid": sid,
            "title": meta["title"],
            "tf": meta["tf"],
            "family": meta["family"],
            "confidence": meta.get("confidence"),
            "filter_id": fid,
            "filter_key": r.get("filter_key"),
            "filter_label": r.get("filter_label_tr") or r.get("filter_label"),
            "blocked": blocked,
            "blocked_pct": (blocked / nm["trades"] * 100.0) if nm["trades"] else 0.0,
        }
        for k, v in nm.items():
            row["n_" + k] = v
        for k, v in sm.items():
            row["s_" + k] = v
        npc = period_counts(normal_days.get((sid, fid), {}))
        row["n_profitWeeks"] = npc["profitWeeks"]
        row["n_lossWeeks"] = npc["lossWeeks"]
        row["n_profitMonths"] = npc["profitMonths"]
        row["n_lossMonths"] = npc["lossMonths"]
        row["delta_retAll"] = row["s_retAll"] - row["n_retAll"]
        row["delta_kasa"] = row["s_kasaAll"] - row["n_kasaAll"]
        rows.append(row)

    # kapsam / filtre satirlari
    def build_scope_rows():
        out = []
        keys = sorted(set(k[0] for k in normal_scope_filter))
        for skey in keys:
            specs_in = [s for s in specs if scope_key(s["sid"]) == skey]
            entry = {
                "key": skey,
                "specs": len(specs_in),
                "tfs": sorted(set(s["tf"] for s in specs_in)),
                "sids": [s["sid"] for s in specs_in],
            }
            for fid, _bit, _key, _label in streams:
                nm = normal_scope_filter.get((skey, fid)) or merge_results_normal([])
                sm = acc_metrics(sing_scope_filter[(skey, fid)])
                b = blocked_scope_filter[(skey, fid)]
                e = {
                    "filter_id": fid,
                    "filter_key": _key,
                    "filter_label": _label,
                    "blocked": b,
                    "blocked_pct": (b / nm["trades"] * 100.0) if nm["trades"] else 0.0,
                }
                for k, v in nm.items():
                    e["n_" + k] = v
                for k, v in sm.items():
                    e["s_" + k] = v
                e["delta_retAll"] = e["s_retAll"] - e["n_retAll"]
                e["delta_kasa"] = e["s_kasaAll"] - e["n_kasaAll"]
                entry.setdefault("filters", []).append(e)
            out.append(entry)
        return out

    filter_rows = []
    for fid, _bit, key, label in streams:
        nm = normal_filter.get(fid) or merge_results_normal([])
        sm = acc_metrics(sing_filter[fid])
        b = blocked_filter[fid]
        row = {
            "filter_id": fid,
            "filter_key": key,
            "filter_label": label,
            "blocked": b,
            "blocked_pct": (b / nm["trades"] * 100.0) if nm["trades"] else 0.0,
        }
        for k, v in nm.items():
            row["n_" + k] = v
        for k, v in sm.items():
            row["s_" + k] = v
        row["delta_retAll"] = row["s_retAll"] - row["n_retAll"]
        row["delta_kasa"] = row["s_kasaAll"] - row["n_kasaAll"]
        filter_rows.append(row)

    # coin kirilimi (baseline)
    coins = []
    for (sid, sym, _), a in sorted(sing_coin.items()):
        nm_n, nm_sum, nm_wins = coin_norm.get((sid, sym), (0, 0.0, 0))
        sm = acc_metrics(a)
        if not sm["trades"] and not nm_n:
            continue
        coins.append({
            "sid": sid,
            "title": spec_by_sid[sid]["title"],
            "family": spec_by_sid[sid]["family"],
            "symbol": sym,
            "n_trades": nm_n,
            "s_trades": sm["trades"],
            "blocked": max(0, nm_n - sm["trades"]),
            "blocked_pct": ((nm_n - sm["trades"]) / nm_n * 100.0) if nm_n else 0.0,
            "n_retAll": (nm_sum / nm_n * 100.0) if nm_n else 0.0,
            "s_retAll": sm["retAll"],
            "n_winRate": (nm_wins / nm_n) if nm_n else 0.0,
            "s_winRate": sm["winRate"],
        })

    # normal/singular toplam (baseline)
    tot_n = normal_totals
    tot_s = acc_metrics(sing_filter["baseline"])
    tot_b = blocked_filter["baseline"]

    payload = {
        "repo": "book-signal-review",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "rule": "Secilen kapsamda ayni coinde ayni anda en fazla bir acik islem. Onceki islem kapanmadan gelen yeni giris sinyali bloke edilir.",
        "scope": args.scope,
        "scope_label": SCOPE_LABEL[args.scope],
        "data": {
            "source": "backtest/filter_layer/results/trades/*.parquet + dashboard_data.json",
            "symbols": len(symbols),
            "specs": len(specs),
            "filters": len(streams),
            "trades_all": int(sum(parquet_base_counts.values())),
            "stake_usd": STAKE,
            "cash_model": "Islem basina sabit 10 USD; retAll = islem basina ortalama getiri (%)",
            "priority": "Ayni giris aninda kisa TF once: 1h > 4h > 1d > 1w, sonra long > short, sonra sid",
            "note": "Motor spec basina filtre basina tek pozisyon tutar; tekil kural bu yuzden family/portfolio kapsaminda anlamlidir.",
        },
        "totals": {
            "normal": tot_n,
            "singular": tot_s,
            "blocked": tot_b,
            "blocked_pct": (tot_b / tot_n["trades"] * 100.0) if tot_n["trades"] else 0.0,
        },
        "filters": filter_rows,
        "scopes": build_scope_rows(),
        "rows": rows,
        "coins": coins,
        "errors": [],
        "overlap_violations": overlap_violations,
        "elapsed_sec": round(time.time() - t0, 1),
    }

    def rnd(obj):
        if isinstance(obj, float):
            return round(obj, 6)
        if isinstance(obj, dict):
            return {k: rnd(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [rnd(v) for v in obj]
        return obj

    payload = rnd(payload)
    with open(os.path.join(args.out, "singular_results.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(args.out, "run_manifest.json"), "w", encoding="utf-8") as f:
        json.dump({
            "repo": payload["repo"],
            "generated_at": payload["generated_at"],
            "scope": args.scope,
            "scope_label": payload["scope_label"],
            "symbols": len(symbols),
            "specs": len(specs),
            "filters": len(streams),
            "normal_trades": tot_n["trades"],
            "singular_trades": tot_s["trades"],
            "blocked": tot_b,
            "blocked_pct": round(payload["totals"]["blocked_pct"], 4),
            "elapsed_sec": payload["elapsed_sec"],
        }, f, ensure_ascii=False, indent=2)

    # CSV
    def write_csv(path, data, cols):
        import csv
        with open(path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            for r in data:
                w.writerow(r)

    row_cols = ["sid", "title", "tf", "family", "confidence", "filter_id", "filter_key", "filter_label",
                "blocked", "blocked_pct", "n_trades", "s_trades", "n_winRate", "s_winRate",
                "n_retAll", "s_retAll", "delta_retAll", "n_ret2026", "s_ret2026",
                "n_winRatio", "s_winRatio", "n_winHoldH", "s_winHoldH",
                "n_profitDays", "s_profitDays", "n_lossDays", "s_lossDays",
                "n_profitWeeks", "s_profitWeeks", "n_lossWeeks", "s_lossWeeks",
                "n_profitMonths", "s_profitMonths", "n_lossMonths", "s_lossMonths",
                "n_maxDD", "s_maxDD", "n_kasaAll", "s_kasaAll", "delta_kasa"]
    write_csv(os.path.join(args.out, "singular_rows.csv"), rows, row_cols)
    write_csv(os.path.join(args.out, "singular_coins.csv"), coins,
              ["sid", "title", "family", "symbol", "n_trades", "s_trades", "blocked", "blocked_pct",
               "n_retAll", "s_retAll", "n_winRate", "s_winRate"])

    print("")
    print(f"[book] kapsam    : {args.scope} ({SCOPE_LABEL[args.scope]})")
    print(f"[book] normal    : {tot_n['trades']:,} islem | WR {tot_n['winRate']*100:.2f}% | ort {tot_n['retAll']:.4f}% | kasa ${tot_n['kasaAll']:.0f}")
    print(f"[book] singular  : {tot_s['trades']:,} islem | WR {tot_s['winRate']*100:.2f}% | ort {tot_s['retAll']:.4f}% | kasa ${tot_s['kasaAll']:.0f}")
    print(f"[book] bloke     : {tot_b:,} ({payload['totals']['blocked_pct']:.2f}%)")
    print(f"[book] yazildi   : {os.path.join(args.out, 'singular_results.json')}")


if __name__ == "__main__":
    main()
