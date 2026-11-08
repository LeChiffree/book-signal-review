import json, re
p = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\dashboard_preview_strategies.html'
h = open(p, encoding='utf-8').read()
i = h.find('const DATA = ') + 13
d, end = json.JSONDecoder().raw_decode(h[i:])
ss = {x['sid']: x for x in d['specs']}
print('RT152C', ss['RT152C'].get('is_duplicate'), ss['RT152C'].get('rule_group_size'))
print('M33', ss['M33'].get('is_duplicate'), ss['M33'].get('rule_group_size'))
print('specs', len(d['specs']), 'unique', d['meta'].get('n_unique_rules'))
print('has uniq filter', '(!uniq||!s.is_duplicate)' in h)
print('checked attr', 'id="uniqOnly" type="checkbox" checked' in h)
# inspect rendered table rows by looking for data-idx of RT152C
idx = ss['RT152C']['idx']
print('idx', idx)
# find any JS anomalies
for pat in ['uniqOnly', 'const uniq=']:
    for m in re.finditer(pat, h):
        print(pat, m.start(), h[m.start():m.start()+120].replace('\n',' '))
