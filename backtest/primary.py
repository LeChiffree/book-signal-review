import json, re, os
from collections import OrderedDict
rows = json.load(open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\sections.json', encoding='utf-8'))
by = OrderedDict()
for i, r in enumerate(rows):
    by.setdefault(r['batch'], []).append((i, r))

excl = ['geri teste alınmaz', 'ilk backtestte ertelenir', 'kataloğa eklenmez', 'kataloğa eklenmez',
        'backtest kuyruğuna alınmaz', 'işlem sinyali olarak ertelendi', 'uygun değil', 'veri koşullu',
        'veri gerektirir', 'hesaplanamaz', 'kapsam dışı', 'sinyal değil', 'strateji değil',
        'pozisyon büyüklüğü', 'risk yönetimi', 'filtre deneyi', 'özellik adayı']
asset = ['SPY', 'QQQ', 'hisse', 'ABD hisse', 'S&P', 'Dow', 'Nasdaq', 'endeks', 'EUR/USD', 'EURUSD',
         'GBP/USD', 'GBPUSD', 'USDJPY', 'USD/JPY', 'USDCHF', 'AUDUSD', 'NZDUSD', 'USDCAD', 'FX ',
         'forex', 'Nifty', 'BankNifty', 'opsiyon', 'option', 'NFP', 'FOMC', 'TÜFE', 'GSYH',
         'earnings', 'kazanç', 'açılış boşluğu', 'gap']

def score(r):
    b = r['body'].lower()
    s = 0
    for k in ['olay:', 'olay olarak', 'kapalı günlük olay', 'kapanmış', 'sinyal:', 'giriş:', 'tetik', 'kural:']:
        if k in b: s += 2
    if 'mekanik' in b: s += 2
    if 'formasyon' in b: s -= 1
    return s

lines = []
for b, items in by.items():
    best = None
    for i, r in items:
        low = r['body'].lower()
        bad = any(k in low for k in excl) or any(k.lower() in low for k in asset)
        sc = score(r)
        if bad: sc -= 10
        if best is None or sc > best[0]:
            best = (sc, i, r)
    sc, i, r = best
    status = 'TEST' if sc >= 2 else ('MAYBE' if sc >= 0 else 'NO')
    lines.append(f"{b}|{status}|{i}|{r['id']}|{r['title'][:110]}")
open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\primary.txt', 'w', encoding='utf-8').write('\n'.join(lines))
from collections import Counter
print(Counter(l.split('|')[1] for l in lines))
print('\n'.join(lines[:20]))
