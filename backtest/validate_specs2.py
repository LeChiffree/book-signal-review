import sys, json, time, traceback
sys.path.insert(0, r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest')
import bookbt as bt

specs = json.load(open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\specs_auto.json', encoding='utf-8'))
tested = [s for s in specs if s.get('status') == 'tested']
for s in tested:
    if s['tf'] == '1m':
        s['tf'] = '5m'
tested = [s for s in tested if s['tf'] in ('1d', '4h')]
print('tested', len(tested), flush=True)

t0 = time.time()
d = bt.prepare_symbol('BTCUSDT', tfs=('4h', '1d'))
print('loaded', round(time.time() - t0, 1), flush=True)

errs = []
for k, s in enumerate(tested):
    t0 = time.time()
    try:
        tr = bt.run_strategy(s, d)
        n = sum(1 for x in tr if 'net' in x)
        if tr and 'error' in tr[0]:
            errs.append((s['idx'], s['sid'], tr[0]['error']))
        dt = time.time() - t0
        if k % 10 == 0 or dt > 5:
            print(k, s['idx'], s['sid'], s['tf'], s['family'], n, round(dt, 2), flush=True)
    except Exception as e:
        errs.append((s['idx'], s['sid'], repr(e)))
print('errors', len(errs), flush=True)
for e in errs[:30]:
    print(e, flush=True)
