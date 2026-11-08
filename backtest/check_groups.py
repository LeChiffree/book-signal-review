import json, hashlib, collections

p = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\specs_final.json'
ss = json.load(open(p, encoding='utf-8'))
tested = [s for s in ss if s.get('status') == 'tested' and s.get('confidence') in ('high', 'medium')]
g = collections.defaultdict(list)
for s in tested:
    key_src = f"{s['tf']}|{s['family']}|{s.get('entry_long')}|{s.get('entry_short')}|{s.get('stop')}|{s.get('time')}"
    key = hashlib.md5(key_src.encode()).hexdigest()
    g[key].append(s)
print('tested', len(tested), 'groups', len(g))
for key, members in g.items():
    if any(m['sid'] in ('P2', 'D1', 'T1', 'JC110A', 'EV207A', 'FB208A') for m in members):
        print(key, len(members), [(m['idx'], m['sid'], m['batch']) for m in members])
