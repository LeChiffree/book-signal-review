import os, sys, time, glob
BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
sys.path.insert(0, BT)
import bookbt as bt

tfs = ('5m', '15m', '1h', '4h', '1d')
syms = bt.symbols()
print('symbols', len(syms), flush=True)
t0 = time.time()
for i, sym in enumerate(syms, 1):
    for tf in tfs:
        p = os.path.join(BT, 'cache', 'htf', f'{sym}_{tf}.parquet')
        if os.path.exists(p):
            continue
        t = time.time()
        df = bt.load_tf(sym, tf)
        print(f'[{i}/{len(syms)}] {sym} {tf} rows={len(df)} {time.time()-t:.1f}s', flush=True)
print('done', round(time.time() - t0, 1), flush=True)
