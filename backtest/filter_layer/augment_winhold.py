import os, glob, json
from collections import defaultdict
import numpy as np
import pandas as pd

ROOT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\filter_layer'
DATA = os.path.join(ROOT, 'dashboard_data.json')
TRADES = os.path.join(ROOT, 'results', 'trades')

D = json.load(open(DATA, encoding='utf-8'))
fmap = {f['id']: int(f['bit']) for f in D['filters']}
fmap['baseline'] = 15
bit2key = {v: k for k, v in fmap.items()}

pairs = defaultdict(set)
for r in D['results']:
    pairs[r['idx']].add(r['filter_key'])

acc = defaultdict(lambda: [0, 0.0])
files = sorted(glob.glob(os.path.join(TRADES, '*.parquet')))
for fi, f in enumerate(files, 1):
    df = pd.read_parquet(f, columns=['idx', 'accepted_mask', 'net', 'entry_time', 'exit_time'])
    if df.empty:
        continue
    accm = df['accepted_mask'].to_numpy(np.int64)
    netm = df['net'].to_numpy()
    hold = (df['exit_time'].to_numpy(np.int64) - df['entry_time'].to_numpy(np.int64)) / 3_600_000.0
    idxs = df['idx'].to_numpy(np.int64)
    win = netm > 0
    for b in sorted(set(fmap.values())):
        m = (((accm >> b) & 1) == 1) & win
        if not m.any():
            continue
        sub_idx = idxs[m]
        sub_h = hold[m]
        u, inv = np.unique(sub_idx, return_inverse=True)
        cnt = np.bincount(inv)
        sm = np.bincount(inv, weights=sub_h)
        key = bit2key[b]
        for i, idx in enumerate(u):
            idx = int(idx)
            if key not in pairs.get(idx, ()):
                continue
            a = acc[(idx, key)]
            a[0] += int(cnt[i])
            a[1] += float(sm[i])
    if fi % 50 == 0:
        print('done', fi, flush=True)

for r in D['results']:
    a = acc.get((r['idx'], r['filter_key']))
    if a and a[0] > 0:
        r['win_hold_h'] = a[1] / a[0]
        r['win_hold_n'] = a[0]
    else:
        r['win_hold_h'] = None
        r['win_hold_n'] = 0

miss = sum(1 for r in D['results'] if not r.get('win_hold_h'))
D['meta']['win_hold_at'] = pd.Timestamp.now('UTC').isoformat()
json.dump(D, open(DATA, 'w', encoding='utf-8'), ensure_ascii=False)
print('rows', len(acc), 'missing', miss, 'wrote', DATA, flush=True)
