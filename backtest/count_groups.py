import json, hashlib, collections

specs = json.load(open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\specs_final.json', encoding='utf-8'))
k = lambda x: '' if x is None else str(x)
groups = collections.defaultdict(list)
for s in specs:
    if s.get('status') != 'tested' or s.get('confidence') not in ('high', 'medium'):
        continue
    key = hashlib.md5(f"{s['tf']}|{s['family']}|{k(s.get('entry_long'))}|{k(s.get('entry_short'))}|{k(s.get('stop'))}|{k(s.get('time'))}".encode()).hexdigest()
    groups[key].append(s)
c = collections.Counter((g[0]['tf'], len(g)) for g in groups.values())
print('unique', len(groups), 'tested', sum(len(g) for g in groups.values()))
print(sorted(c.items()))
print('unique by tf', collections.Counter(g[0]['tf'] for g in groups.values()))
