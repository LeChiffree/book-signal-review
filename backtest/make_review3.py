import json
p = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\specs_auto3.json'
s = json.load(open(p, encoding='utf-8'))
out = []
for x in s:
    if x['status'] != 'tested':
        continue
    out.append('|'.join([
        str(x['idx']), x['batch'], x['sid'], x['tf'], x['family'],
        x['title'][:85], str(x.get('entry_long'))[:120]
    ]))
open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\review_specs3.txt', 'w', encoding='utf-8').write('\n'.join(out))
print(len(out))
