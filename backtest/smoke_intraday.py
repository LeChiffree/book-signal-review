import sys, json, time
sys.path.insert(0, r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest')
import bookbt as bt

specs = json.load(open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\specs_final.json', encoding='utf-8'))
tested = [s for s in specs if s.get('status') == 'tested' and s.get('confidence') in ('high', 'medium')]
sel = [s for s in tested if s['tf'] in ('5m', '15m', '1h')][:40]
print('specs', len(sel), flush=True)

t0 = time.time()
d = bt.prepare_symbol('BTCUSDT', tfs=('5m', '15m', '1h', '4h', '1d'), load_minute=True)
print('loaded', round(time.time() - t0, 1), flush=True)
print('tfs', {k: len(v) for k, v in d['tf'].items()}, flush=True)

errs = []
for i, s in enumerate(sel):
    t0 = time.time()
    try:
        tr = bt.run_strategy(s, d)
        if tr and 'error' in tr[0]:
            errs.append((s['idx'], s['sid'], tr[0]['error']))
            print('ERR', s['idx'], s['sid'], tr[0]['error'], flush=True)
        else:
            print(i, s['idx'], s['sid'], s['tf'], s['family'], len(tr), round(time.time() - t0, 2), flush=True)
    except Exception as e:
        errs.append((s['idx'], s['sid'], repr(e)))
        print('EXC', s['idx'], s['sid'], repr(e), flush=True)
print('errors', len(errs), flush=True)
