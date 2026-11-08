import os, json
import numpy as np
import pandas as pd

ROOT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\filter_layer'
D = json.load(open(os.path.join(ROOT, 'dashboard_data.json'), encoding='utf-8'))
rows = D['results']


def pct(x, d=2):
    return f'{x*100:,.{d}f}%'


def table(rs, cols, heads):
    out = ['| ' + ' | '.join(heads) + ' |', '|' + '|'.join(['---'] * len(heads)) + '|']
    for r in rs:
        out.append('| ' + ' | '.join(str(r.get(c, '')) for c in cols) + ' |')
    return '\n'.join(out)


kept = [r for r in rows if r['kept']]
base = [r for r in rows if r['filter_key'] == 'baseline']
base_ok = [r for r in base if r['n'] >= 30]
strong = [r for r in kept if r['n'] >= 50 and r['symbols'] >= 15 and r['median_symbol_net'] > 0]
strong = sorted(strong, key=lambda r: r['median_symbol_net'], reverse=True)
top = strong[:20]

print('rows', len(rows), 'kept', len(kept), 'baseline', len(base), 'strong', len(strong))
print('best', [(r['sid'], r['filter_label_tr'], round(r['median_symbol_net']*100,2), round(r['avg_net']*100,2), r['n']) for r in top[:10]])

# filter comparison
frows = []
for f in D['filters']:
    rr = [r for r in rows if r['filter_key'] == f['id']]
    kk = [r for r in rr if r['kept']]
    frows.append({
        'filter': f['label_tr'],
        'tested': len(rr),
        'positive': len(kk),
        'median_positive_avg': pct(np.median([r['avg_net'] for r in kk]), 2) if kk else '—',
        'trades': int(sum(r['n'] for r in rr)),
    })

# baseline vs best filter per strategy
by = {}
for r in rows:
    by.setdefault(r['idx'], {'base': None, 'filters': []})
    if r['filter_key'] == 'baseline':
        by[r['idx']]['base'] = r
    else:
        by[r['idx']]['filters'].append(r)
improved = 0
for v in by.values():
    if not v['base'] or v['base']['n'] < 30:
        continue
    fs = [r for r in v['filters'] if r['kept'] and r['n'] >= 30]
    if fs and max(r['avg_net'] for r in fs) > v['base']['avg_net']:
        improved += 1

lines = []
lines.append('# Filtre Laboratuvarı — 525 Sembol Raporu')
lines.append('')
lines.append(f"**Kapsam:** 525 sembol · 120 benzersiz kural test edildi (116’sı işlem üretti; 1d/4h/1h/1w) · 14 filtre · {len(rows)} strateji × filtre sonucu")
lines.append('')
lines.append('**Maliyet:** 5 bps taker/side, 2 bps slippage/side, tarihsel 8s funding. Sinyal stratejinin kendi timeframe’inde; giriş/stop/hedef 1m OHLC’de.')
lines.append('')
lines.append('## Özet')
lines.append('')
lines.append(f'- Pozitif ortalama işlem başı getiri (toplam veya 2026): **{len(kept)} / {len(rows)}** sonuç.')
lines.append(f'- En az 50 işlem, 15 sembol ve pozitif medyan sembol neti koşulunu geçen: **{len(strong)}** sonuç.')
lines.append('- Eleme: yalnızca **hem toplam hem 2026 takvimi** işlem başı neti negatif olan sonuçlar dışarıda bırakıldı.')
lines.append(f'- Filtresiz bazı en az 30 işlem olan {len(base_ok)} stratejiden **{improved}** tanesinde en az bir filtre bazdan daha iyi ortalama net üretti.')
lines.append('- 5m/15m filtre katmanına alınmadı; brüt kenar zaten negatif ve 219M işlemde filtre maliyeti karşılamıyor.')
lines.append('')
lines.append('## Filtre bazında pozitiflik')
lines.append('')
lines.append(table(frows, ['filter', 'tested', 'positive', 'median_positive_avg', 'trades'],
                   ['Filtre', 'Test', 'Pozitif', 'Pozitif medyan ort.', 'İşlem']))
lines.append('')
lines.append('## En güçlü sonuçlar (medyan sembol neti)')
lines.append('')
lines.append(table([
    {'sid': r['sid'], 'tf': r['tf'], 'filter': r['filter_label_tr'], 'n': r['n'],
     'symbols': r['symbols'], 'avg': pct(r['avg_net'], 2), 'ret26': pct(r['ret_2026'], 2),
     'median': pct(r['median_symbol_net'], 2),
     'pf': '∞' if r['profit_factor'] >= 999 else f"{r['profit_factor']:.2f}",
     'portfolio': pct(r['portfolio_net'], 1)}
    for r in top
], ['sid', 'tf', 'filter', 'n', 'symbols', 'avg', 'ret26', 'median', 'pf', 'portfolio'],
   ['SID', 'TF', 'Filtre', 'İşlem', 'Sembol', 'Ort. net', '2026', 'Med. sembol', 'PF', 'Portföy']))
lines.append('')
lines.append('## Yöntem notu')
lines.append('')
lines.append('- Her filtre ayrı bir giriş koşulu olarak, kendi non-overlap durumuyla simüle edildi; filtrelenmiş işlemler sonradan seçilmedi.')
lines.append('- Filtreler tek tek test edildi. “Tüm kombinasyonlar” burada **strateji × filtre** kombinasyonlarıdır; 14 filtrenin tüm 2^14 alt kümesi değildir.')
lines.append('- `fng_greed` ve `fng_fear` aynı anda doğru olamaz; bu nedenle 14 filtrenin AND’i tanımsızdır.')
lines.append('- Eleme kuralı: toplam işlem başı net **ve** 2026 takvimi işlem başı net aynı anda negatifse sonuç dışarıda bırakılır.')
lines.append('- 5m/15m baz sonuçları ana raporda ayrıca durur; bu filtre laboratuvarı 1d/4h/1h/1w kuralarına odaklanır.')
lines.append('')
lines.append('## Dosyalar')
lines.append('')
lines.append('- `filter_dashboard.html` — interaktif dashboard')
lines.append('- `dashboard_data.json` — tüm sonuçlar ve günlük seriler')
lines.append('- `strategy_filter_metrics.csv` — tablo')
lines.append('- `results/trades/*.parquet` — kabul edilmiş işlemler')
lines.append('')

out = os.path.join(ROOT, 'FILTER_REPORT.md')
open(out, 'w', encoding='utf-8').write('\n'.join(lines))
print('wrote', out)
