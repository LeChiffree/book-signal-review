import sys, json, time, traceback
sys.path.insert(0, r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest')
import bookbt as bt
from collections import Counter

specs = json.load(open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\specs_auto.json', encoding='utf-8'))
tested = [s for s in specs if s.get('status') == 'tested']
print('tested', len(tested), Counter(s['tf'] for s in tested))

# use 5m instead of 1m base
for s in tested:
    if s['tf'] == '1m':
        s['tf'] = '5m'

t0 = time.time()
d = bt.prepare_symbol('BTCUSDT', tfs=('5m', '15m', '1h', '4h', '1d'))
print('loaded', round(time.time() - t0, 1))

errs = []
rows = []
for s in tested:
    t0 = time.time()
    try:
        tr = bt.run_strategy(s, d)
        n = sum(1 for x in tr if 'net' in x)
        if tr and 'error' in tr[0]:
            errs.append((s['idx'], s['sid'], tr[0]['error']))
        rows.append((s['idx'], s['sid'], s['tf'], s['family'], n, round(time.time() - t0, 2)))
    except Exception as e:
        errs.append((s['idx'], s['sid'], repr(e)))
print('errors', len(errs))
for e in errs[:30]:
    print(e)
print('no trades', sum(1 for r in rows if r[4] == 0))
print('slowest', sorted(rows, key=lambda x: -x[5])[:10])
print('total time', round(time.time() - t0, 1))
