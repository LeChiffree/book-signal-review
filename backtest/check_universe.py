import os, glob
import pandas as pd

root = r'D:\1mDataBinance'
for sub in ['active_525/futures_bars/1h', 'active_525/futures_bars/4h', '1m']:
    p = os.path.join(root, sub)
    if sub == '1m':
        syms = [d for d in os.listdir(p) if os.path.isdir(os.path.join(p, d))]
    else:
        syms = [f[:-8] for f in os.listdir(p) if f.endswith('.parquet')]
    print(sub, 'symbols', len(syms), 'first', syms[:5])

# inspect one 1h/4h/1m
for f in [r'D:\1mDataBinance\active_525\futures_bars\1h\BTCUSDT.parquet',
          r'D:\1mDataBinance\active_525\futures_bars\4h\BTCUSDT.parquet',
          r'D:\1mDataBinance\1m\BTCUSDT\BTCUSDT-1m-2026-08.parquet']:
    print('\n', f, os.path.getsize(f))
    df = pd.read_parquet(f)
    print(df.shape, df.columns.tolist())
    print(df.head(2).to_string())
    print(df.tail(2).to_string())
