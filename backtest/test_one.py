import sys, time, json
sys.path.insert(0, r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest')
import bookbt as bt

spec = dict(
    id='A1', tf='1d', direction='both',
    entry_long="(close > ref(highest(high,20),1)) & (adx14>20) & (pdi>mdi) & (ref(count(adx14<20,10),1)>=10)",
    entry_short="(close < ref(lowest(low,20),1)) & (adx14>20) & (mdi>pdi) & (ref(count(adx14<20,10),1)>=10)",
    exit_long="close < donchian(high,low,20)[1]",
    exit_short="close > donchian(high,low,20)[0]",
    stop_atr=2.0, time_bars=14, atr_n=14,
)
t0=time.time()
d = bt.prepare_symbol('BTCUSDT', tfs=('1d',))
print('load', time.time()-t0, {k:len(v) for k,v in d['tf'].items()}, {k:len(v) for k,v in d['m1'].items()})
t0=time.time()
tr = bt.run_strategy(spec, d)
print('run', time.time()-t0, 'trades', len(tr))
import pandas as pd
for x in tr[:5]:
    if 'error' in x: print(x); continue
    print(pd.to_datetime(x['entry_time'],unit='ms'), pd.to_datetime(x['exit_time'],unit='ms'), x['side'], round(x['net']*100,3), x['reason'], x['bars_held'])
print(bt.metrics([t for t in tr if 'net' in t]))
