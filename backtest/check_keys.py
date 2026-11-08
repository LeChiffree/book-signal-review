import json, hashlib

sp = {s['sid']: s for s in json.load(open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\specs_final.json', encoding='utf-8'))}
d = json.load(open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\dashboard_data.json', encoding='utf-8'))
r = {s['sid']: s for s in d['specs']}
for sid in ['P2', 'D1', 'T1', 'JC110A', 'EV207A', 'FB208A']:
    s = sp[sid]
    a = r[sid]
    k1 = hashlib.md5(f"{s['tf']}|{s['family']}|{s.get('entry_long')}|{s.get('entry_short')}|{s.get('stop')}|{s.get('time')}".encode()).hexdigest()
    k2 = hashlib.md5(f"{a['tf']}|{a['family']}|{a['rule_long']}|{a['rule_short']}|{s.get('stop')}|{s.get('time')}".encode()).hexdigest()
    print(sid, k1, k2, k1 == k2)
    print('  spec entry:', repr(s.get('entry_long')))
    print('  agg rule  :', repr(a['rule_long']))
