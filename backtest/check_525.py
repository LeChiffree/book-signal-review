import os, glob
import pandas as pd

root = r'D:\1mDataBinance'
m1_syms = sorted(d for d in os.listdir(os.path.join(root, '1m')) if os.path.isdir(os.path.join(root, '1m', d)))
h1_syms = sorted(os.path.basename(f)[:-8] for f in glob.glob(os.path.join(root, 'active_525', 'futures_bars', '1h', '*.parquet')))
h4_syms = sorted(os.path.basename(f)[:-8] for f in glob.glob(os.path.join(root, 'active_525', 'futures_bars', '4h', '*.parquet')))
print('1m symbols', len(m1_syms))
print('1h symbols', len(h1_syms))
print('4h symbols', len(h4_syms))
print('1m only', len(set(m1_syms) - set(h1_syms)), sorted(set(m1_syms) - set(h1_syms))[:10])
print('1h only', len(set(h1_syms) - set(m1_syms)), sorted(set(h1_syms) - set(m1_syms))[:10])
# date coverage for a few new symbols
for sym in ['0GUSDT', '1000BONKUSDT', 'BTCUSDT', 'ZECUSDT', 'XRPUSDT']:
    f1 = os.path.join(root, 'active_525', 'futures_bars', '1h', sym + '.parquet')
    f4 = os.path.join(root, 'active_525', 'futures_bars', '4h', sym + '.parquet')
    if os.path.exists(f1):
        df = pd.read_parquet(f1, columns=['open_time'])
        print(sym, '1h', pd.to_datetime(df.open_time.min(), unit='ms'), pd.to_datetime(df.open_time.max(), unit='ms'), len(df))
    if os.path.exists(f4):
        df = pd.read_parquet(f4, columns=['open_time'])
        print(sym, '4h', pd.to_datetime(df.open_time.min(), unit='ms'), pd.to_datetime(df.open_time.max(), unit='ms'), len(df))
    # count 1m files and first/last
    fs = sorted(glob.glob(os.path.join(root, '1m', sym, sym + '-1m-*')))
    if fs:
        print(sym, '1m files', len(fs), os.path.basename(fs[0]), os.path.basename(fs[-1]))
