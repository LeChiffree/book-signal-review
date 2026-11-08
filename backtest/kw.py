import json, re, os
from collections import Counter
rows = json.load(open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\sections.json', encoding='utf-8'))
kws = ['SMA','EMA','WMA','LWMA','SMMA','HMA','KAMA','RSI','MACD','ADX','DI','ATR','Bollinger','BB','Keltner','Donchian','Ichimoku','Tenkan','Kijun','bulut','Supertrend','stokastik','Stoch','CCI','OBV','MFI','CMF','VWAP','AVWAP','pivot','fib','Fibonacci','Heikin','HA','Aroon','Williams','%R','momentum','Momentum','ROC','EMV','Coppock','TRI','RWI','Chande','EFI','AO','AC','SAR','Camarilla','CPR','VWMA','KAMA','GMMA','OsMA','HA','engulf','yutan','çekiç','doji','pin','inside','iç bar','gap','boşluk','seans','session','Asya','Londra','New York','SPY','hisse','FX','EUR','GBP','USDJPY','endeks','breadth','genişlik','korelasyon','portföy','momentum rotasyon']
alltext = '\n'.join(r['body'] for r in rows)
for k in kws:
    print(f'{k:12s} {alltext.count(k):5d}')
print('\n--- timeframes per section ---')
tfs = ['M1','M5','M15','M30','H1','H4','D1','W1','haftalık','günlük','aylık']
for i,r in enumerate(rows):
    b=r['body']
    found=[t for t in tfs if re.search(r'(?<![A-Za-z0-9])'+re.escape(t)+r'(?![A-Za-z0-9])', b)]
print(Counter(t for r in rows for t in tfs if re.search(r'(?<![A-Za-z0-9])'+re.escape(t)+r'(?![A-Za-z0-9])', r['body'])))
