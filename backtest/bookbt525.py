"""
525-symbol data adapter for bookbt.

Signals stay on the strategy timeframe. Execution and stop/target tracking
remain the existing 1-minute engine in bookbt.

Sources:
  1h / 4h : D:\\1mDataBinance\\active_525\\futures_bars\\{tf}\\{sym}.parquet
  1d      : resampled from 1h
  1w      : resampled from 1d (bookbt.resample_weekly)
  5m/15m  : resampled from the local 1m archive
  funding : D:\\1mDataBinance\\active_525\\funding\\{sym}.parquet
"""
import os
import glob
import numpy as np
import pandas as pd

import bookbt as bt

ROOT = bt.DATA
BARS = os.path.join(ROOT, 'active_525', 'futures_bars')
FUND = os.path.join(ROOT, 'active_525', 'funding')

COMMON = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time',
          'quote_asset_volume', 'ts']


def symbols():
    return sorted(os.path.basename(f)[:-8] for f in
                  glob.glob(os.path.join(BARS, '1h', '*.parquet')))


def _norm(df):
    if df is None or df.empty:
        return pd.DataFrame(columns=COMMON)
    d = df.copy()
    if 'quote_asset_volume' not in d.columns:
        if 'quote_volume' in d.columns:
            d['quote_asset_volume'] = d['quote_volume']
        else:
            d['quote_asset_volume'] = 0.0
    d['ts'] = pd.to_datetime(d['open_time'], unit='ms', utc=True)
    d = d[(d['ts'] >= bt.START) & (d['ts'] <= bt.END)]
    for c in ['open', 'high', 'low', 'close', 'volume', 'quote_asset_volume']:
        d[c] = pd.to_numeric(d[c], errors='coerce')
    d = d.dropna(subset=['open', 'high', 'low', 'close'])
    d = d.drop_duplicates('open_time').sort_values('open_time').reset_index(drop=True)
    if 'close_time' not in d.columns:
        d['close_time'] = d['open_time']
    return d[COMMON]


def _from_bars(sym, tf):
    f = os.path.join(BARS, tf, f'{sym}.parquet')
    if not os.path.exists(f):
        return pd.DataFrame(columns=COMMON)
    return _norm(pd.read_parquet(f))


def _resample(df, rule, tf_ms):
    if df is None or df.empty:
        return pd.DataFrame(columns=COMMON)
    d = df.set_index('ts')
    agg = d.resample(rule, label='left', closed='left').agg(
        open=('open', 'first'), high=('high', 'max'), low=('low', 'min'),
        close=('close', 'last'), volume=('volume', 'sum'),
        quote_asset_volume=('quote_asset_volume', 'sum'))
    agg = agg.dropna(subset=['open', 'high', 'low', 'close']).reset_index()
    agg = agg.rename(columns={'index': 'ts'})
    agg['open_time'] = (agg['ts'].astype('datetime64[ns, UTC]').astype('int64') // 1_000_000).astype('int64')
    agg['close_time'] = agg['open_time'] + tf_ms - 1
    return agg[COMMON]


def load_tf(sym, tf, m1=None):
    if tf in ('1h', '4h'):
        return _from_bars(sym, tf)
    if tf == '1d':
        h = _from_bars(sym, '1h')
        return _resample(h, '1D', 86_400_000)
    if tf in ('5m', '15m'):
        if m1 is None:
            m1 = bt.load_1m(sym)
        if not m1:
            return pd.DataFrame(columns=COMMON)
        df = pd.DataFrame({k: m1[k] for k in ['open_time', 'open', 'high', 'low',
                                              'close', 'volume', 'quote_asset_volume']})
        df['ts'] = pd.to_datetime(df['open_time'], unit='ms', utc=True)
        tf_ms = bt.TF_MS[tf]
        rule = '5min' if tf == '5m' else '15min'
        return _resample(df, rule, tf_ms)
    return pd.DataFrame(columns=COMMON)


def load_funding(sym):
    f = os.path.join(FUND, f'{sym}.parquet')
    if not os.path.exists(f):
        return np.array([], dtype=np.int64), np.array([], dtype=np.float64)
    d = pd.read_parquet(f, columns=['fundingTime', 'fundingRate']).dropna()
    d = d.sort_values('fundingTime')
    return d['fundingTime'].to_numpy(dtype=np.int64), d['fundingRate'].to_numpy(dtype=np.float64)


def prepare_symbol(sym, tfs=('5m', '15m', '1h', '4h', '1d'), load_minute=True):
    need_m1 = load_minute or any(tf in ('5m', '15m') for tf in tfs)
    m1 = bt.load_1m(sym) if need_m1 else {}
    d = {'symbol': sym, 'tf': {}, 'htf': {}, 'm1': m1}
    for tf in tfs:
        df = load_tf(sym, tf, m1)
        if not df.empty:
            d['tf'][tf] = df
            d['htf'][tf] = df
    if '1d' in d['tf']:
        w = bt.resample_weekly(d['tf']['1d'])
        if not w.empty:
            d['tf']['1w'] = w
            d['htf']['1w'] = w
    if load_minute:
        d['fund_t'], d['fund_r'] = load_funding(sym)
    return d


def install():
    bt.symbols = symbols
    bt.load_tf = load_tf
    bt.load_funding = load_funding
    bt.prepare_symbol = prepare_symbol
