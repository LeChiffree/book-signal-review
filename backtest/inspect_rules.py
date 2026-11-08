import json

p = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\specs_final.json'
ss = json.load(open(p, encoding='utf-8'))
d = {s['sid']: s for s in ss}
for sid in ['P2', 'D1', 'T1', 'JC110A', 'EV207A', 'FB208A', 'M33', 'RT152C', 'G1', 'EC139A']:
    s = d.get(sid)
    if not s:
        continue
    print('\n', sid, s['tf'], s['family'], s.get('confidence'))
    print(' long:', s.get('entry_long'))
    print(' short:', s.get('entry_short'))
    print(' stop/time:', s.get('stop'), s.get('time'), 'params:', s.get('params'))
