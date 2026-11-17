#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Singular-Backtest dogrulama — Book Signal Review.

Kontroller:
  1. 1738 dashboard satirinin tamami payload'da var mi?
  2. Her satirda singular + bloke == normal islem sayisi.
  3. Parquet kabul maskesi sayimlari dashboard `n` degerleriyle birebir mi?
  4. Secilen kapsam + filtre icin rastgele orneklerde acik islem cakismasi var mi?
  5. Toplamlar: singular + bloke == normal; kasaAll == sumR * 10.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import random
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DASH = os.path.join(ROOT, "backtest", "filter_layer", "dashboard_data.json")
TRADES = os.path.join(ROOT, "backtest", "filter_layer", "results", "trades")
RESULT = os.path.join(HERE, "results", "singular_results.json")
TF_ORDER = {"1h": 0, "4h": 1, "1d": 2, "1w": 3}

errors = []


def check(cond, msg):
    if cond:
        print(f"  [OK]   {msg}")
    else:
        print(f"  [FAIL] {msg}")
        errors.append(msg)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=8)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    with open(DASH, encoding="utf-8") as f:
        dash = json.load(f)
    with open(RESULT, encoding="utf-8") as f:
        pay = json.load(f)

    specs = {s["sid"]: s for s in dash["specs"]}
    scope = pay["scope"]
    rows = pay["rows"]
    by_key = {(r["sid"], str(r["filter_id"])): r for r in rows}

    print("== Kapsam ==")
    print(f"  scope={scope} | {pay['scope_label']}")

    print("== 1) Satir kapsamasi ==")
    check(len(rows) == len(dash["results"]), f"payload satir sayisi {len(rows)} == dashboard {len(dash['results'])}")
    missing = [r for r in dash["results"] if (r["sid"], str(r["filter_id"])) not in by_key]
    check(not missing, f"eksik satir yok ({len(missing)} eksik)")

    print("== 2) Tekil + bloke == normal ==")
    bad = []
    for r in rows:
        if int(r["s_trades"]) + int(r["blocked"]) != int(r["n_trades"]):
            bad.append((r["sid"], r["filter_id"], r["n_trades"], r["s_trades"], r["blocked"]))
    check(not bad, f"tum satirlarda singular + bloke == normal ({len(bad)} ihlal)")
    if bad:
        for b in bad[:5]:
            print("    ", b)

    print("== 3) Parquet kabul sayimlari (dashboard n) ==")
    streams = [("baseline", 15)]
    for i, f in enumerate(dash["filters"]):
        streams.append((str(i), i))
    parquet_counts = {}
    files = sorted(glob.glob(os.path.join(TRADES, "*.parquet")))

    scope_of = {}
    for s in dash["specs"]:
        if scope == "family":
            scope_of[s["sid"]] = s["family"]
        elif scope == "portfolio":
            scope_of[s["sid"]] = "BOOK"
        else:
            scope_of[s["sid"]] = s["sid"]
    tfo_of = {s["sid"]: TF_ORDER.get(s["tf"], 9) for s in dash["specs"]}
    bit_of = {"baseline": 15}
    for i in range(len(dash["filters"])):
        bit_of[str(i)] = i

    rng = random.Random(args.seed)
    groups = sorted({(scope_of[s["sid"]], str(r["filter_id"])) for s in dash["specs"] for r in rows if r["sid"] == s["sid"]})
    pick = set(rng.sample(groups, min(args.samples, len(groups))))
    acc_counts = {}
    checked_trades = 0

    for path in files:
        df = pd.read_parquet(path, columns=["sid", "entry_time", "exit_time", "accepted_mask"])
        if df.empty:
            continue
        mask = np.asarray(df["accepted_mask"], dtype=np.int64)
        for fid, bit in streams:
            sel = ((mask >> bit) & 1) == 1
            if not sel.any():
                continue
            for sid, c in df.loc[sel].groupby("sid").size().items():
                parquet_counts[(sid, fid)] = parquet_counts.get((sid, fid), 0) + int(c)
        # ornek gruplar: ayni dosya icinde kapsam + filtre
        df = df.assign(sk=df["sid"].map(scope_of), tfo=df["sid"].map(tfo_of))
        for skey, fid in pick:
            bit = bit_of[fid]
            g = df[((mask >> bit) & 1) == 1]
            g = g[g["sk"] == skey]
            if g.empty:
                continue
            g = g.sort_values(["entry_time", "tfo", "sid"], ascending=[True, True, True], kind="stable")
            last_exit = -1
            for et, xt, sid in zip(g["entry_time"].values, g["exit_time"].values, g["sid"].values):
                if et < last_exit:
                    continue
                last_exit = int(xt)
                acc_counts[(sid, fid)] = acc_counts.get((sid, fid), 0) + 1
                checked_trades += 1

    mism = []
    for r in rows:
        key = (r["sid"], str(r["filter_id"]))
        pc = parquet_counts.get(key, 0)
        if pc != int(r["n_trades"]):
            mism.append((key, pc, int(r["n_trades"]), pc - int(r["n_trades"])))
    check(not mism, f"parquet sayimlari dashboard n ile ayni ({len(mism)} uyusmazlik)")
    if mism:
        for m in mism[:5]:
            print("    ", m[:3], "fark", m[3])

    print("== 4) Ornek kapsam denetimi ==")
    bad4 = []
    for key, cnt in acc_counts.items():
        ref = by_key.get(key)
        if ref is None or int(ref["s_trades"]) != cnt:
            bad4.append((key, cnt, None if ref is None else ref["s_trades"]))
    check(not bad4, f"{len(pick)} ornek grupta {checked_trades:,} kabul islemi payload ile ayni ({len(bad4)} uyusmazlik)")

    print("== 5) Toplamlar ==")
    t = pay["totals"]
    check(t["singular"]["trades"] + t["blocked"] == t["normal"]["trades"],
          f"singular {t['singular']['trades']:,} + bloke {t['blocked']:,} == normal {t['normal']['trades']:,}")
    for who in ("normal", "singular"):
        m = t[who]
        ok = abs(m["kasaAll"] - m["sumR"] * 10.0) < 1e-3
        check(ok, f"{who}: kasaAll == sumR * 10")
        ok2 = (m["trades"] == 0) or (abs(m["retAll"] - m["sumR"] / m["trades"] * 100.0) < 1e-6)
        check(ok2, f"{who}: retAll == ortalama net * 100")

    print("")
    if errors:
        print(f"SONUC: {len(errors)} HATA")
        sys.exit(1)
    print("SONUC: TUM KONTROLLER GECTI")


if __name__ == "__main__":
    main()
