import sys, json, time, traceback
sys.path.insert(0, r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest')
import bookbt as bt

specs = json.load(open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\specs_final.json', encoding='utf-8'))
tested = [s for s in specs if s.get('status') == 'tested']
sel = [s for s in tested if s['tf'] in ('1d', '1w', '4h') and s.get('confidence') == 'high'][:60]
print('specs', len(sel), flush=True)

t0 = time.time()
d = bt.prepare_symbol('BTCUSDT', tfs=('4h', '1d'), load_minute=True)
print('loaded', round(time.time() - t0, 1), flush=True)
print('tfs', {k: len(v) for k, v in d['tf'].items()}, 'm1', len(d['m1']), flush=True)
if '1w' in d['tf']:
    w = d['tf']['1w']
    print('weekly head', w[['open_time', 'open', 'close']].head(3).to_dict('records'), flush=True)
    print('weekly tail', w[['open_time', 'open', 'close']].tail(3).to_dict('records'), flush=True)

errs = []
for i, s in enumerate(sel):
    t0 = time.time()
    try:
        tr = bt.run_strategy(s, d)
        if tr and 'error' in tr[0]:
            errs.append((s['idx'], s['sid'], tr[0]['error']))
            print('ERR', s['idx'], s['sid'], tr[0]['error'], flush=True)
        else:
            n = len(tr)
            dt = time.time() - t0
            if i % 10 == 0 or dt > 3:
                print(i, s['idx'], s['sid'], s['tf'], s['family'], n, round(dt, 2), flush=True)
    except Exception as e:
        errs.append((s['idx'], s['sid'], repr(e)))
        print('EXC', s['idx'], s['sid'], repr(e), flush=True)
print('errors', len(errs), flush=True)
for e in errs[:20]:
    print(e, flush=True)
