import os, re, json, glob
root = r'D:\Paper_ML_BSH\analysis\book_signal_review'
files = sorted(glob.glob(os.path.join(root, 'batch_*', 'STRATEGIES.md')))
rows = []
for f in files:
    t = open(f, encoding='utf-8').read()
    batch = os.path.basename(os.path.dirname(f))
    # split by ### headings
    parts = re.split(r'\n(?=### )', t)
    for p in parts:
        m = re.match(r'###\s+(.+?)\s*$', p.split('\n', 1)[0])
        if not m:
            continue
        title = m.group(1).strip()
        body = p.split('\n', 1)[1] if '\n' in p else ''
        # only up to next ## or ###
        body = re.split(r'\n## ', body)[0]
        rows.append({'batch': batch, 'id': title.split('—')[0].strip(), 'title': title, 'body': body.strip()})
print('total sections', len(rows))
print('batches with >=1', len({r['batch'] for r in rows}))
from collections import Counter
print(Counter(r['batch'] for r in rows).most_common(5))
json.dump(rows, open(os.path.join(root, 'backtest', 'sections.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for i, r in enumerate(rows):
    print(f"{i:03d} {r['batch']} | {r['id']} | {r['title'][:95]}")
