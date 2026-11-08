import sys, time, os, json
sys.path.insert(0, r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest')
import bookbt as bt
from concurrent.futures import ProcessPoolExecutor, as_completed

SPECS = [
 dict(id='A1', tf='1d', direction='both',
  entry_long="(close > ref(highest(high,20),1)) & (adx14>20) & (pdi>mdi) & (ref(count(adx14<20,10),1)>=10)",
  entry_short="(close < ref(lowest(low,20),1)) & (adx14>20) & (mdi>pdi) & (ref(count(adx14<20,10),1)>=10)",
  exit_long="close < donchian(high,low,20)[1]", exit_short="close > donchian(high,low,20)[0]",
  stop_atr=2.0, time_bars=14),
 dict(id='A2', tf='1d', direction='both',
  entry_long="(adx14>20)&(adx14>ref(adx14,1))&(pdi>mdi)&(ref(count(low<=ema(close,20),5),1)>=1)&(close>ref(high,1))",
  entry_short="(adx14>20)&(adx14>ref(adx14,1))&(mdi>pdi)&(ref(count(high>=ema(close,20),5),1)>=1)&(close<ref(low,1))",
  exit_long="close<ema(close,20)", exit_short="close>ema(close,20)", stop_atr=2.0, time_bars=7),
 dict(id='B1', tf='1d', direction='both',
  entry_long="(close>sma(close,200))&(ref(count(pctb(close,5,1)<0,2),1)>=2)&(adx(high,low,close,10)[0]>30)&(std(log(close/ref(close,1)),100)*sqrt(365)>0.30)",
  entry_short="(close<sma(close,200))&(ref(count(pctb(close,5,1)>1,2),1)>=2)&(adx(high,low,close,10)[0]>30)&(std(log(close/ref(close,1)),100)*sqrt(365)>0.30)",
  exit_long="pctb(close,5,1)>1", exit_short="pctb(close,5,1)<0", stop_atr=3.0, time_bars=14, limit_entry_pct=0.04, limit_window_bars=1),
 dict(id='E1', tf='1d', direction='both',
  entry_long="(close>ema(close,20))&(ref(count(close<ema(close,20),10),1)>=3)&(ref(count(low>=ema(close,20),5),1)>=1)&(close>ref(pivh(high,2,2).ffill(),1))&(pdi>mdi)",
  entry_short="(close<ema(close,20))&(ref(count(close>ema(close,20),10),1)>=3)&(ref(count(high<=ema(close,20),5),1)>=1)&(close<ref(pivl(low,2,2).ffill(),1))&(mdi>pdi)",
  stop_mode='signal_low', stop_buffer_atr=0.1, time_bars=14),
]
TFS = ('1d',)


def work(sym):
    t0 = time.time()
    d = bt.prepare_symbol(sym, tfs=TFS)
    out = {}
    for s in SPECS:
        tr = bt.run_strategy(s, d)
        out[s['id']] = tr
    return sym, out, time.time() - t0


if __name__ == '__main__':
    syms = bt.symbols()[:4]
    t0 = time.time()
    with ProcessPoolExecutor(max_workers=4) as ex:
        for sym, out, dt in ex.map(work, syms):
            print(sym, round(dt, 1), {k: len(v) for k, v in out.items()}, {k: sum(1 for x in v if 'net' in x) for k, v in out.items()})
    print('total', round(time.time() - t0, 1))
