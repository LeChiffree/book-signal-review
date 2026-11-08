import sys, time, pandas as pd
sys.path.insert(0, r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest')
import bookbt as bt

specs = [
 dict(id='A2', tf='1d', direction='both',
  entry_long="(adx14>20)&(adx14>ref(adx14,1))&(pdi>mdi)&(ref(count(low<=ema(close,20),5),1)>=1)&(close>ref(high,1))",
  entry_short="(adx14>20)&(adx14>ref(adx14,1))&(mdi>pdi)&(ref(count(high>=ema(close,20),5),1)>=1)&(close<ref(low,1))",
  exit_long="close<ema(close,20)", exit_short="close>ema(close,20)",
  stop_atr=2.0, time_bars=7),
 dict(id='B1', tf='1d', direction='both',
  entry_long="(close>sma(close,200))&(ref(count(pctb(close,5,1)<0,2),1)>=2)&(adx(high,low,close,10)[0]>30)&(std(log(close/ref(close,1)),100)*sqrt(365)>0.30)",
  entry_short="(close<sma(close,200))&(ref(count(pctb(close,5,1)>1,2),1)>=2)&(adx(high,low,close,10)[0]>30)&(std(log(close/ref(close,1)),100)*sqrt(365)>0.30)",
  exit_long="pctb(close,5,1)>1", exit_short="pctb(close,5,1)<0",
  stop_atr=3.0, time_bars=14, limit_entry_pct=0.04, limit_window_bars=1),
 dict(id='E1', tf='1d', direction='both',
  entry_long="(close>ema(close,20))&(ref(count(close<ema(close,20),10),1)>=3)&(ref(count(low>=ema(close,20),5),1)>=1)&(close>ref(pivh(high,2,2).ffill(),1))&(pdi>mdi)",
  entry_short="(close<ema(close,20))&(ref(count(close>ema(close,20),10),1)>=3)&(ref(count(high<=ema(close,20),5),1)>=1)&(close<ref(pivl(low,2,2).ffill(),1))&(mdi>pdi)",
  stop_mode='signal_low', stop_buffer_atr=0.1, time_bars=14),
]

d = bt.prepare_symbol('BTCUSDT', tfs=('1d',))
for spec in specs:
    t0=time.time(); tr=bt.run_strategy(spec,d); m=bt.metrics([x for x in tr if 'net' in x])
    print(spec['id'], 'trades', len(tr), 'run', round(time.time()-t0,2), {k:round(v,4) if isinstance(v,float) else v for k,v in m.items() if k in ('trades','win_rate','avg_net','total_net','max_dd','profit_factor','avg_hold_h')})
    if tr and 'error' in tr[0]: print(tr[0])
