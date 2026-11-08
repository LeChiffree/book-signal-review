import json, re
rows = json.load(open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\sections.json', encoding='utf-8'))
excl_kw = ['geri teste alınmaz','ilk backtestte ertelenir','kataloğa eklenmez','strateji kataloğuna eklenmez',
           'backtest kuyruğuna alınmaz','işlem sinyali olarak ertelendi','uygun değil','veri koşullu',
           'veri yok','veri gerektirir','hesaplanamaz','kapsam dışı','portföy kuralı','pozisyon büyüklüğü',
           'risk yönetimi','filtre deneyi','özellik adayı','sinyal değil','strateji değil','tekrarı','aynı olaydır']
asset_kw = ['SPY','QQQ','hisse','ABD hisse','S&P','Dow','Nasdaq','endeks','EUR/USD','EURUSD','GBP/USD','GBPUSD',
            'USDJPY','USD/JPY','USDCHF','AUDUSD','NZDUSD','USDCAD','FX ','forex','Nifty','BankNifty','option','opsiyon',
            'NFP','FOMC','TÜFE','GSYH','earnings','kazanç','seans boşluğu','açılış boşluğu','gap']
cand=[]
for i,r in enumerate(rows):
    b=r['body']; low=b.lower(); title=r['title'].lower()
    reasons=[]
    for k in excl_kw:
        if k in low: reasons.append(k)
    for k in asset_kw:
        if k.lower() in low: reasons.append('asset:'+k)
    has_event = any(k in low for k in ['olay:','olay olarak','kapalı günlük olay','kapanmış','sinyal:','giriş:','tetik'])
    cand.append((i,r['batch'],r['id'],has_event,reasons))
ok=[c for c in cand if c[3] and not c[4]]
print('event+noexcl',len(ok))
print('event but excluded',len([c for c in cand if c[3] and c[4]]))
print('no event',len([c for c in cand if not c[3]]))
for c in ok[:20]: print(c[0],c[2])
json.dump([{'i':c[0],'batch':c[1],'id':c[2],'event':c[3],'reasons':c[4]} for c in cand],open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\classify.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
