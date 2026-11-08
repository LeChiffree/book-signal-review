import os, sys, json, glob, math, collections
import numpy as np
import pandas as pd

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
ROOT = os.path.join(BT, 'filter_layer')
TRADES = os.path.join(ROOT, 'results', 'trades')
DATA = os.path.join(ROOT, 'data')
OUT = os.path.join(ROOT, 'dashboard_data.json')
ALLOC_N = 525
BASE_BIT = 15
N_FILTERS = 14

HOLD_LABELS = ['<1g', '1-3g', '3-7g', '7-14g', '14-35g', '35-65g', '65g+']
HOLD_BINS = [1, 3, 7, 14, 35, 65]


def load_defs():
    return json.load(open(os.path.join(DATA, 'filter_defs.json'), encoding='utf-8'))


def load_specs():
    specs = json.load(open(os.path.join(BT, 'specs_final.json'), encoding='utf-8'))
    return {s['idx']: s for s in specs}


def new_acc():
    return {
        'n': 0, 'total': 0.0, 'pos': 0.0, 'neg': 0.0,
        'wins': 0, 'gross': 0.0, 'sym_nets': [],
        'ret26_n': 0, 'ret26': 0.0,
        'hold': np.zeros((7, 4), dtype=float),   # n, pos, neg, net
        'long': np.zeros(5, dtype=float),         # n, total, pos, neg, wins
        'short': np.zeros(5, dtype=float),
        'scatter': [],
    }


def add_side(arr, net):
    arr[0] += len(net)
    arr[1] += float(net.sum())
    arr[2] += float(net[net > 0].sum())
    arr[3] += float(net[net < 0].sum())
    arr[4] += int((net > 0).sum())


def main():
    defs = load_defs()
    filters = defs['filters']
    specs = load_specs()
    files = sorted(glob.glob(os.path.join(TRADES, '*.parquet')))
    print('trade files', len(files), flush=True)

    acc = {}
    for k, f in enumerate(files, 1):
        df = pd.read_parquet(f, columns=['idx', 'accepted_mask', 'net', 'gross', 'symbol',
                                         'entry_time', 'exit_time', 'side'])
        if df.empty:
            continue
        for idx, g in df.groupby('idx', sort=False):
            idx = int(idx)
            for fid in list(range(N_FILTERS)) + ['baseline']:
                bit = BASE_BIT if fid == 'baseline' else int(fid)
                sub = g[(g['accepted_mask'].astype(np.int64) & (1 << bit)) != 0]
                if sub.empty:
                    continue
                key = (idx, str(fid))
                a = acc.setdefault(key, new_acc())
                net = sub['net'].to_numpy(dtype=float)
                a['n'] += len(net)
                a['total'] += float(net.sum())
                a['pos'] += float(net[net > 0].sum())
                a['neg'] += float(net[net < 0].sum())
                a['wins'] += int((net > 0).sum())
                a['gross'] += float(sub['gross'].sum())
                a['sym_nets'].append(float(net.mean()))

                exit_t = sub['exit_time'].to_numpy(dtype=np.int64)
                entry_t = sub['entry_time'].to_numpy(dtype=np.int64)
                yr = pd.to_datetime(exit_t, unit='ms', utc=True).year.to_numpy()
                m26 = yr == 2026
                if m26.any():
                    a['ret26_n'] += int(m26.sum())
                    a['ret26'] += float(net[m26].sum())

                hold_days = (exit_t - entry_t) / 86_400_000.0
                b = np.searchsorted(HOLD_BINS, hold_days, side='right')
                for bi in range(7):
                    mm = b == bi
                    if not mm.any():
                        continue
                    x = net[mm]
                    a['hold'][bi, 0] += float(len(x))
                    a['hold'][bi, 1] += float(x[x > 0].sum())
                    a['hold'][bi, 2] += float(x[x < 0].sum())
                    a['hold'][bi, 3] += float(x.sum())

                side_arr = sub['side'].to_numpy(dtype=int)
                if (side_arr == 1).any():
                    add_side(a['long'], net[side_arr == 1])
                if (side_arr == -1).any():
                    add_side(a['short'], net[side_arr == -1])

                if len(a['scatter']) < 800:
                    need = 800 - len(a['scatter'])
                    if len(net) <= need:
                        take = np.arange(len(net))
                    else:
                        take = np.linspace(0, len(net) - 1, need).astype(int)
                    for j in take:
                        a['scatter'].append([round(float(hold_days[j]), 4), round(float(net[j]), 6)])
        if k % 50 == 0:
            print('acc', k, 'pairs', len(acc), flush=True)

    # keep if total per-trade > 0 OR 2026 per-trade > 0; baseline is always materialised.
    selected = set()
    for (idx, fid), a in acc.items():
        r26 = (a['ret26'] / a['ret26_n']) if a['ret26_n'] else None
        keep = (a['n'] and a['total'] / a['n'] > 0) or (r26 is not None and r26 > 0)
        if keep or fid == 'baseline':
            selected.add((idx, fid))
    print('results', len(acc), 'selected daily', len(selected), flush=True)

    daily = {key: {} for key in selected}
    selected_by_idx = collections.defaultdict(list)
    for idx, fid in selected:
        selected_by_idx[idx].append(fid)

    for k, f in enumerate(files, 1):
        df = pd.read_parquet(f, columns=['idx', 'accepted_mask', 'net', 'exit_time'])
        if df.empty:
            continue
        groups = {int(k): g for k, g in df.groupby('idx', sort=False)}
        for idx, fids in selected_by_idx.items():
            g = groups.get(idx)
            if g is None or g.empty:
                continue
            for fid in fids:
                bit = BASE_BIT if fid == 'baseline' else int(fid)
                sub = g[(g['accepted_mask'].astype(np.int64) & (1 << bit)) != 0]
                if sub.empty:
                    continue
                d = pd.DataFrame({
                    'day': (sub['exit_time'].astype('int64') // 86_400_000).astype('int64'),
                    'net': sub['net'].astype(float).to_numpy(),
                })
                d['pos'] = np.where(d['net'] > 0, d['net'], 0.0)
                d['neg'] = np.where(d['net'] < 0, d['net'], 0.0)
                gg = d.groupby('day', sort=True).agg(n=('net', 'size'), pos=('pos', 'sum'),
                                                     neg=('neg', 'sum'), net=('net', 'sum'))
                for day, row in gg.iterrows():
                    arr = daily[(idx, fid)].get(int(day), [0, 0.0, 0.0, 0.0])
                    arr[0] += int(row['n']); arr[1] += float(row['pos'])
                    arr[2] += float(row['neg']); arr[3] += float(row['net'])
                    daily[(idx, fid)][int(day)] = arr
        if k % 50 == 0:
            print('daily', k, flush=True)

    results = []
    for (idx, fid), a in acc.items():
        n = a['n']
        if not n:
            continue
        total = a['total']
        avg = total / n
        ret26 = (a['ret26'] / a['ret26_n']) if a['ret26_n'] else None
        kept = bool((avg > 0) or (ret26 is not None and ret26 > 0))
        dmap = daily.get((idx, fid), {})
        days = sorted(dmap)
        eq = 1.0; peak = 1.0; mdd = 0.0
        daily_arr = []
        for day in days:
            cnt, pos, neg, net = dmap[day]
            eq *= (1.0 + net / ALLOC_N)
            peak = max(peak, eq)
            mdd = min(mdd, eq / peak - 1.0)
            daily_arr.append([day, cnt, round(pos, 8), round(neg, 8), round(net, 8)])
        sym = np.array(a['sym_nets'], dtype=float)
        sp = specs.get(idx, {})
        fdef = next((x for x in filters if int(x['bit']) == int(fid)), None) if fid != 'baseline' else None
        hold = [[int(a['hold'][i, 0]), round(float(a['hold'][i, 1]), 8),
                 round(float(a['hold'][i, 2]), 8), round(float(a['hold'][i, 3]), 8)]
                for i in range(7)]
        results.append({
            'idx': int(idx),
            'sid': sp.get('sid', ''),
            'batch': sp.get('batch', ''),
            'title': sp.get('title', ''),
            'tf': sp.get('tf', ''),
            'family': sp.get('family', ''),
            'confidence': sp.get('confidence', ''),
            'filter_id': str(fid),
            'filter_key': 'baseline' if fid == 'baseline' else (fdef['id'] if fdef else str(fid)),
            'filter_label': 'Baseline (no filter)' if fid == 'baseline' else (fdef['label'] if fdef else str(fid)),
            'filter_label_tr': 'Filtresiz baz' if fid == 'baseline' else (fdef.get('label_tr', fdef['label']) if fdef else str(fid)),
            'n': int(n), 'symbols': int(len(sym)),
            'avg_net': float(avg), 'total_net': float(total),
            'pos_sum': float(a['pos']), 'neg_sum': float(a['neg']),
            'win_rate': float(a['wins'] / n),
            'profit_factor': float(a['pos'] / abs(a['neg'])) if a['neg'] else (float('inf') if a['pos'] else 0.0),
            'gross': float(a['gross']),
            'fee_drag': float((a['gross'] - total) / n),
            'portfolio_net': float(eq - 1.0),
            'max_dd': float(mdd),
            'median_symbol_net': float(np.median(sym)) if len(sym) else 0.0,
            'pct_symbols_positive': float((sym > 0).mean()) if len(sym) else 0.0,
            'ret_2026': (float(ret26) if ret26 is not None else None),
            'ret_2026_n': int(a['ret26_n']),
            'kept': kept,
            'daily': daily_arr,
            'hold_hist': hold,
            'long': [int(a['long'][0]), round(float(a['long'][1]), 8), round(float(a['long'][2]), 8),
                     round(float(a['long'][3]), 8), int(a['long'][4])],
            'short': [int(a['short'][0]), round(float(a['short'][1]), 8), round(float(a['short'][2]), 8),
                      round(float(a['short'][3]), 8), int(a['short'][4])],
            'scatter': a['scatter'],
        })
    print('result rows', len(results), flush=True)

    fstats = []
    for f in filters:
        rows = [r for r in results if r['filter_id'] == str(f['bit'])]
        kept = [r for r in rows if r['kept']]
        fstats.append({
            'bit': f['bit'], 'id': f['id'], 'label': f['label'], 'label_tr': f['label_tr'],
            'n_results': len(rows), 'n_positive': len(kept),
            'median_avg_net': float(np.median([r['avg_net'] for r in kept])) if kept else None,
            'n_trades': int(sum(r['n'] for r in rows)),
        })

    kept = [r for r in results if r['kept']]
    base = [r for r in results if r['filter_id'] == 'baseline']
    data = {
        'meta': {
            'n_symbols': 525, 'n_specs': len({r['idx'] for r in results}),
            'n_filters': len(filters), 'n_results': len(results),
            'n_kept': len(kept), 'n_baseline': len(base),
            'alloc_n': ALLOC_N, 'fee_bps': 5.0, 'slip_bps': 2.0,
            'hold_labels': HOLD_LABELS,
            'start': defs.get('start'), 'end': defs.get('end'),
            'generated_at': pd.Timestamp.now('UTC').isoformat(),
        },
        'filters': filters,
        'filter_stats': fstats,
        'specs': [
            {**{k: sp.get(k, '') for k in ['idx', 'sid', 'batch', 'title', 'tf', 'family', 'confidence']},
             'rule_long': sp.get('entry_long', ''),
             'rule_short': sp.get('entry_short', ''),
             'rule_group_size': sp.get('rule_group_size', 1)}
            for sp in [specs[i] for i in sorted({r['idx'] for r in results})]
        ],
        'results': results,
    }
    json.dump(data, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
    csv_rows = []
    for r in results:
        csv_rows.append({k: v for k, v in r.items() if k not in ('daily', 'hold_hist', 'long', 'short', 'scatter')})
    pd.DataFrame(csv_rows).to_csv(os.path.join(ROOT, 'strategy_filter_metrics.csv'),
                                  index=False, encoding='utf-8-sig')
    print('wrote', OUT, len(json.dumps(data)), 'chars', flush=True)


if __name__ == '__main__':
    main()
