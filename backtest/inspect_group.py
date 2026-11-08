import json

p = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\dashboard_data.json'
d = json.load(open(p, encoding='utf-8'))
for s in d['specs']:
    if s['sid'] in ['P2', 'D1', 'T1', 'JC110A', 'EV207A', 'FB208A']:
        print(s['sid'], repr(s['rule_long']), repr(s['rule_short']), s.get('rule_key'), s.get('rule_group_size'), s.get('is_duplicate'))
