import os, re, glob, json
root = r'D:\Paper_ML_BSH\analysis\book_signal_review'
files = sorted(glob.glob(os.path.join(root, 'batch_*', 'STRATEGIES.md')))
print('files', len(files))
out = []
for f in files:
    t = open(f, encoding='utf-8').read()
    heads = [l.strip() for l in t.splitlines() if l.startswith('#')]
    out.append({'batch': os.path.basename(os.path.dirname(f)), 'len': len(t), 'heads': heads})
sample = out[:2] + out[40:42] + out[100:102] + out[150:152] + out[200:202] + out[-2:]
for o in sample:
    print('\n===', o['batch'], o['len'])
    for h in o['heads'][:25]:
        print('  ', h[:130])
print('\nheading counts:')
from collections import Counter
c = Counter()
for o in out:
    c[sum(1 for h in o['heads'] if h.startswith('## '))] += 1
print(c)
json.dump(out, open(os.path.join(root, 'backtest', 'heads.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
