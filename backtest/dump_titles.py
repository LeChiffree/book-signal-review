import os, re, json
root = r'D:\Paper_ML_BSH\analysis\book_signal_review'
rows = json.load(open(os.path.join(root, 'backtest', 'sections.json'), encoding='utf-8'))
lines = []
for i, r in enumerate(rows):
    body = r['body']
    flags = []
    for kw in ['ertelendi', 'alınmaz', 'uygun değil', 'eklenmez', 'aynı olay', 'tekrarı',
               'bekliyor', 'varyant', 'ablation', 'araştırma adayı', 'kataloğa']:
        if kw in body.lower():
            flags.append(kw)
    # first bold rule line
    first = ''
    for ln in body.splitlines():
        if ln.strip().startswith('- **'):
            first = re.sub(r'\*\*', '', ln.strip())[:160]
            break
    lines.append(f"{i:03d}|{r['batch']}|{r['id']}|{r['title'][:110]}|{','.join(flags)}|{first}")
open(os.path.join(root, 'backtest', 'titles.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
print(len(lines))
