"""
Build daily regime masks for the filter layer.

Bits:
 0 BTC above 200d SMA
 1 BTC 30d return > 0
 2 BTC 20d vol <= trailing 1y median
 3 Fear & Greed >= 50
 4 Fear & Greed <= 25
 5 30d dollar volume >= cross-sectional median
 6 Breadth: >=50% of symbols above 50d SMA
 7 Symbol 30d return > BTC 30d return
 8 Symbol above 200d SMA
 9 Symbol within 20% of 90d high
10 Symbol 20d vol <= cross-sectional median

Trade-level bits (added at signal bar):
11 volume > 1.5x trailing 20-bar median
12 last funding rate > 0
13 last funding rate < 0
"""
import os, json, glob
import numpy as np
import pandas as pd

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
OUT = os.path.join(BT, 'filter_layer', 'data')
os.makedirs(OUT, exist_ok=True)

import sys
sys.path.insert(0, BT)
import bookbt525

bookbt525.install()
import bookbt as bt

FNG = os.path.join(OUT, 'fear_greed.csv')


def load_fng():
    d = pd.read_csv(FNG)
    d['date'] = pd.to_datetime(d['date'], utc=True).dt.normalize()
    d = d.drop_duplicates('date').set_index('date').sort_index()
    return d['fng'].astype(float)


def main():
    syms = bt.symbols()
    print('symbols', len(syms), flush=True)
    closes = {}
    qvs = {}
    for k, sym in enumerate(syms, 1):
        df = bt.load_tf(sym, '1d')
        if df.empty:
            continue
        d = df.copy()
        d['date'] = pd.to_datetime(d['ts'], utc=True).dt.normalize()
        d = d.drop_duplicates('date').set_index('date').sort_index()
        closes[sym] = pd.to_numeric(d['close'], errors='coerce')
        qvs[sym] = pd.to_numeric(d['quote_asset_volume'], errors='coerce')
        if k % 50 == 0:
            print('loaded', k, flush=True)

    close = pd.DataFrame(closes).sort_index()
    qv = pd.DataFrame(qvs).sort_index()
    print('panel', close.shape, close.index.min(), close.index.max(), flush=True)

    sma50 = close.rolling(50, min_periods=30).mean()
    sma200 = close.rolling(200, min_periods=120).mean()
    ret30 = close / close.shift(30) - 1.0
    vol20 = np.log(close).diff().rolling(20, min_periods=10).std()
    hi90 = close.rolling(90, min_periods=30).max()
    adv30 = qv.rolling(30, min_periods=10).median()

    breadth = (close > sma50).sum(axis=1) / (close.notna() & sma50.notna()).sum(axis=1).replace(0, np.nan)
    liq_med = adv30.median(axis=1)
    vol_med = vol20.median(axis=1)

    btc = close['BTCUSDT']
    btc_sma200 = btc.rolling(200, min_periods=120).mean()
    btc_ret30 = btc / btc.shift(30) - 1.0
    btc_vol20 = np.log(btc).diff().rolling(20, min_periods=10).std()
    btc_vol_med = btc_vol20.rolling(252, min_periods=60).median()

    fng = load_fng().reindex(close.index).ffill()

    # common daily conditions
    c0 = btc > btc_sma200
    c1 = btc_ret30 > 0
    c2 = btc_vol20 <= btc_vol_med
    c3 = fng >= 50
    c4 = fng <= 25
    c6 = breadth >= 0.5

    rows = []
    for sym in close.columns:
        c = close[sym]
        m = pd.DataFrame(index=close.index)
        m['c0'] = c0
        m['c1'] = c1
        m['c2'] = c2
        m['c3'] = c3
        m['c4'] = c4
        m['c5'] = adv30[sym] >= liq_med
        m['c6'] = c6
        m['c7'] = ret30[sym] > btc_ret30
        m['c8'] = c > sma200[sym]
        m['c9'] = c >= 0.8 * hi90[sym]
        m['c10'] = vol20[sym] <= vol_med
        mask = np.zeros(len(m), dtype=np.uint16)
        for bit in range(11):
            mask |= (m[f'c{bit}'].fillna(False).to_numpy(dtype=bool).astype(np.uint16) << bit)
        # pandas may store datetime64 in us in newer versions; force ns epoch.
        day_close = pd.DatetimeIndex(m.index) + pd.Timedelta(hours=23, minutes=59, seconds=59)
        ts_ms = (day_close.astype('datetime64[ns, UTC]').asi8 // 1_000_000).astype('int64')
        out = pd.DataFrame({
            'symbol': sym,
            'ts': ts_ms,
            'mask': mask.astype(np.uint16),
        })
        rows.append(out)

    daily = pd.concat(rows, ignore_index=True)
    daily = daily[daily['ts'].notna()]
    daily.to_parquet(os.path.join(OUT, 'daily_masks.parquet'), index=False)
    print('daily_masks', daily.shape, 'saved', flush=True)

    # diagnostics
    last = pd.DataFrame({
        'btc_trend': c0, 'btc_mom': c1, 'btc_calm': c2,
        'fng_greed': c3, 'fng_fear': c4, 'breadth': c6,
    }).dropna(how='all')
    last.to_csv(os.path.join(OUT, 'market_regimes.csv'))
    print('market regimes', last.shape, last.mean(numeric_only=True).to_dict(), flush=True)

    defs = [
        {'bit': 0, 'id': 'btc_trend', 'label': 'BTC > 200d SMA', 'label_tr': 'BTC 200g SMA üzerinde'},
        {'bit': 1, 'id': 'btc_mom', 'label': 'BTC 30d return > 0', 'label_tr': 'BTC 30g getirisi pozitif'},
        {'bit': 2, 'id': 'btc_calm', 'label': 'BTC vol <= 1y median', 'label_tr': 'BTC oynaklığı 1y medyanın altında'},
        {'bit': 3, 'id': 'fng_greed', 'label': 'Fear & Greed >= 50', 'label_tr': 'Korku/Açgözlülük >= 50'},
        {'bit': 4, 'id': 'fng_fear', 'label': 'Fear & Greed <= 25', 'label_tr': 'Korku/Açgözlülük <= 25'},
        {'bit': 5, 'id': 'liquidity', 'label': 'Liquidity >= cross-sectional median', 'label_tr': 'Likidite medyanın üzerinde'},
        {'bit': 6, 'id': 'breadth', 'label': 'Breadth >= 50%', 'label_tr': 'Piyasa genişliği >= %50'},
        {'bit': 7, 'id': 'rel_strength', 'label': 'Symbol 30d > BTC 30d', 'label_tr': 'Sembol 30g getirisi BTC’den güçlü'},
        {'bit': 8, 'id': 'symbol_trend', 'label': 'Symbol > 200d SMA', 'label_tr': 'Sembol 200g SMA üzerinde'},
        {'bit': 9, 'id': 'near_high', 'label': 'Symbol >= 80% of 90d high', 'label_tr': 'Sembol 90g zirvesinin %80’inde'},
        {'bit': 10, 'id': 'low_vol', 'label': 'Symbol vol <= cross-sectional median', 'label_tr': 'Sembol oynaklığı medyanın altında'},
        {'bit': 11, 'id': 'volume_surge', 'label': 'Volume > 1.5x 20-bar median', 'label_tr': 'Hacim 20 barlık medyanın 1.5 katı'},
        {'bit': 12, 'id': 'funding_pos', 'label': 'Last funding > 0', 'label_tr': 'Son funding pozitif'},
        {'bit': 13, 'id': 'funding_neg', 'label': 'Last funding < 0', 'label_tr': 'Son funding negatif'},
    ]
    json.dump({'filters': defs, 'generated_at': pd.Timestamp.utcnow().isoformat(),
               'n_symbols': len(syms), 'start': str(close.index.min()), 'end': str(close.index.max())},
              open(os.path.join(OUT, 'filter_defs.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved defs', flush=True)


if __name__ == '__main__':
    main()
