import json
p = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\specs_final.json'
s = json.load(open(p, encoding='utf-8'))
out = []
for x in s:
    if x['status'] != 'tested':
        continue
    out.append('|'.join([
        str(x['idx']), x['batch'], x['sid'], x['tf'], x['family'], x['confidence'],
        x['title'][:75], str(x.get('entry_long'))[:110]
    ]))
open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\review_final.txt', 'w', encoding='utf-8').write('\n'.join(out))
print(len(out))
