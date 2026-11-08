"""
Book strategy review backtester.
Signals are generated on the strategy timeframe from completed bars.
Execution is simulated on 1-minute OHLC with fees, slippage and funding.
"""
from __future__ import annotations
import os, re, json, math, glob, ast
import numpy as np
import pandas as pd

DATA = r'D:\1mDataBinance'
BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
START = pd.Timestamp('2022-08-01', tz='UTC')
END = pd.Timestamp('2026-08-31 23:59:59', tz='UTC')
EXEC_END = pd.Timestamp('2026-10-18', tz='UTC')

TF_MS = {'1m': 60_000, '5m': 300_000, '15m': 900_000, '1h': 3_600_000,
         '4h': 14_400_000, '1d': 86_400_000, '1w': 604_800_000}

FEE = 0.0005          # 5 bps per side, Binance USDT-M taker
SLIP = 0.0002         # 2 bps per side
USE_HTF_CACHE = True


# ----------------------------------------------------------------------------- data
def symbols():
    return sorted(os.path.basename(p) for p in glob.glob(os.path.join(DATA, '1d', '*')))


def load_tf(sym: str, tf: str) -> pd.DataFrame:
    cache = os.path.join(BT, 'cache', 'htf', f'{sym}_{tf}.parquet')
    if USE_HTF_CACHE and os.path.exists(cache):
        return pd.read_parquet(cache)
    files = sorted(glob.glob(os.path.join(DATA, tf, sym, f'{sym}-{tf}-*.csv')))
    if not files:
        return pd.DataFrame()
    parts = []
    for f in files:
        try:
            parts.append(pd.read_csv(f, usecols=['open_time', 'open', 'high', 'low', 'close',
                                                 'volume', 'close_time', 'quote_asset_volume']))
        except Exception:
            continue
    if not parts:
        return pd.DataFrame()
    df = pd.concat(parts, ignore_index=True)
    df = df.drop_duplicates('open_time').sort_values('open_time').reset_index(drop=True)
    df['ts'] = pd.to_datetime(df['open_time'], unit='ms', utc=True)
    df = df[(df['ts'] >= START) & (df['ts'] <= END)].reset_index(drop=True)
    if USE_HTF_CACHE and not df.empty:
        os.makedirs(os.path.dirname(cache), exist_ok=True)
        df.to_parquet(cache, index=False)
    return df


def load_1m(sym: str) -> dict:
    cache_dir = os.path.join(BT, 'cache', '1m')
    os.makedirs(cache_dir, exist_ok=True)
    cache = os.path.join(cache_dir, f'{sym}.parquet')
    if os.path.exists(cache):
        df = pd.read_parquet(cache)
    else:
        files = sorted(glob.glob(os.path.join(DATA, '1m', sym, f'{sym}-1m-*')))
        parts = []
        for f in files:
            m = re.search(r'-1m-(\d{4})-(\d{2})', f)
            if m:
                y, mo = int(m.group(1)), int(m.group(2))
                if (y, mo) < (2022, 7) or (y, mo) > (2026, 10):
                    continue
            try:
                if f.endswith('.csv'):
                    parts.append(pd.read_csv(f, usecols=['open_time', 'open', 'high', 'low', 'close',
                                                         'volume', 'quote_asset_volume']))
                else:
                    parts.append(pd.read_parquet(f, columns=['open_time', 'open', 'high', 'low', 'close',
                                                             'volume', 'quote_asset_volume']))
            except Exception:
                continue
        if not parts:
            return {}
        df = pd.concat(parts, ignore_index=True).drop_duplicates('open_time').sort_values('open_time')
        df = df[(df['open_time'] >= int(START.timestamp() * 1000)) &
                (df['open_time'] <= int(EXEC_END.timestamp() * 1000))].reset_index(drop=True)
        for c in ['open', 'high', 'low', 'close', 'volume', 'quote_asset_volume']:
            df[c] = pd.to_numeric(df[c], errors='coerce')
        df = df.dropna(subset=['open', 'high', 'low', 'close']).reset_index(drop=True)
        df.to_parquet(cache, compression='zstd', index=False)
    return {c: df[c].to_numpy(dtype=np.float64) for c in
            ['open_time', 'open', 'high', 'low', 'close', 'volume', 'quote_asset_volume']}


def resample_weekly(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()
    d = df.copy()
    d.index = pd.to_datetime(d['ts'], utc=True)
    agg = d.resample('W-MON', label='left', closed='left').agg(
        open=('open', 'first'), high=('high', 'max'), low=('low', 'min'),
        close=('close', 'last'), volume=('volume', 'sum'),
        quote_asset_volume=('quote_asset_volume', 'sum'))
    agg = agg.dropna(subset=['open', 'high', 'low', 'close']).reset_index()
    agg = agg.rename(columns={'index': 'ts'})
    # ts is datetime64[ms] in recent pandas; normalise to ns before converting to ms epoch
    agg['open_time'] = (agg['ts'].astype('datetime64[ns, UTC]').astype('int64') // 1_000_000).astype('int64')
    agg['close_time'] = agg['open_time'] + 7 * 86_400_000 - 1
    return agg[['open_time', 'open', 'high', 'low', 'close', 'volume',
                'close_time', 'quote_asset_volume', 'ts']]


def load_funding(sym: str):
    f = os.path.join(DATA, '151_M', 'binance_futures', 'funding', f'{sym}.csv')
    if not os.path.exists(f):
        return np.array([], dtype=np.int64), np.array([], dtype=np.float64)
    d = pd.read_csv(f, usecols=['funding_time', 'funding_rate'])
    d = d.dropna().sort_values('funding_time')
    return d['funding_time'].to_numpy(dtype=np.int64), d['funding_rate'].to_numpy(dtype=np.float64)


# ------------------------------------------------------------------------ indicators
def _s(x):
    return x if isinstance(x, pd.Series) else pd.Series(x)


def sma(x, n):
    return _s(x).rolling(int(n), min_periods=int(n)).mean()


def ema(x, n):
    return _s(x).ewm(span=int(n), adjust=False, min_periods=int(n)).mean()


def rma(x, n):
    return _s(x).ewm(alpha=1.0 / int(n), adjust=False, min_periods=int(n)).mean()


def wma(x, n):
    n = int(n)
    w = np.arange(1, n + 1, dtype=float)
    return _s(x).rolling(n, min_periods=n).apply(lambda a: np.dot(a, w) / w.sum(), raw=True)


def lwma(x, n, shift=0):
    return wma(_s(x).shift(int(shift)), n)


def hma(x, n):
    n = int(n)
    return wma(2 * wma(x, n // 2) - wma(x, n), int(math.sqrt(n)))


def kama(x, n=10, fast=2, slow=30):
    x = _s(x)
    change = (x - x.shift(n)).abs()
    vol = x.diff().abs().rolling(n).sum()
    er = (change / vol.replace(0, np.nan)).fillna(0)
    sc = (er * (2 / (fast + 1) - 2 / (slow + 1)) + 2 / (slow + 1)) ** 2
    out = np.empty(len(x)); out[:] = np.nan
    vals = x.to_numpy(dtype=float)
    scv = sc.to_numpy(dtype=float)
    for i in range(1, len(x)):
        if np.isnan(vals[i]):
            continue
        prev = vals[i - 1] if np.isnan(out[i - 1]) else out[i - 1]
        out[i] = prev + scv[i] * (vals[i] - prev) if not np.isnan(scv[i]) else prev
    return pd.Series(out, index=x.index)


def rsi(x, n=14, method='wilder'):
    x = _s(x)
    d = x.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    if method == 'sma':
        au = up.rolling(int(n), min_periods=int(n)).mean()
        ad = dn.rolling(int(n), min_periods=int(n)).mean()
    else:
        au = rma(up, n); ad = rma(dn, n)
    rs = au / ad.replace(0, np.nan)
    out = 100 - 100 / (1 + rs)
    return out.where(~((ad == 0) & (au > 0)), 100).where(~((ad == 0) & (au == 0)), 50)


def true_range(h, l, c):
    h, l, c = _s(h), _s(l), _s(c)
    pc = c.shift(1)
    return pd.concat([h - l, (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)


def atr(h, l, c, n=14, method='wilder'):
    tr = true_range(h, l, c)
    if method == 'sma':
        return tr.rolling(int(n), min_periods=int(n)).mean()
    return rma(tr, n)


def adx(h, l, c, n=14):
    h, l, c = _s(h), _s(l), _s(c)
    up = h.diff(); dn = -l.diff()
    plus_dm = pd.Series(np.where((up > dn) & (up > 0), up, 0.0), index=h.index)
    minus_dm = pd.Series(np.where((dn > up) & (dn > 0), dn, 0.0), index=h.index)
    tr = true_range(h, l, c)
    atr_ = rma(tr, n)
    pdi = 100 * rma(plus_dm, n) / atr_.replace(0, np.nan)
    mdi = 100 * rma(minus_dm, n) / atr_.replace(0, np.nan)
    dx = 100 * (pdi - mdi).abs() / (pdi + mdi).replace(0, np.nan)
    return rma(dx, n), pdi, mdi


def macd(x, fast=12, slow=26, sig=9):
    x = _s(x)
    line = ema(x, fast) - ema(x, slow)
    signal = ema(line, sig)
    return line, signal, line - signal


def bb(x, n=20, k=2.0):
    x = _s(x)
    mid = x.rolling(int(n), min_periods=int(n)).mean()
    sd = x.rolling(int(n), min_periods=int(n)).std(ddof=0)
    return mid, mid + k * sd, mid - k * sd, sd


def donchian(h, l, n=20):
    h, l = _s(h), _s(l)
    return h.rolling(int(n), min_periods=int(n)).max().shift(1), l.rolling(int(n), min_periods=int(n)).min().shift(1)


def pctb(x, n=20, k=2.0):
    mid, up, lo, sd = bb(x, n, k)
    return (x - lo) / (up - lo).replace(0, np.nan)


def bbw(x, n=20, k=2.0):
    mid, up, lo, sd = bb(x, n, k)
    return (up - lo) / mid.replace(0, np.nan)


def keltner(c, h, l, n=20, mult=1.5):
    mid = ema(c, n)
    a = atr(h, l, c, n)
    return mid, mid + mult * a, mid - mult * a


def stoch(h, l, c, k=14, d=3, smooth=3):
    h, l, c = _s(h), _s(l), _s(c)
    hh = h.rolling(int(k), min_periods=int(k)).max()
    ll = l.rolling(int(k), min_periods=int(k)).min()
    raw = 100 * (c - ll) / (hh - ll).replace(0, np.nan)
    kk = raw.rolling(int(smooth), min_periods=int(smooth)).mean()
    dd = kk.rolling(int(d), min_periods=int(d)).mean()
    return kk, dd


def cci(h, l, c, n=20):
    tp = (_s(h) + _s(l) + _s(c)) / 3
    ma = tp.rolling(int(n), min_periods=int(n)).mean()
    md = (tp - ma).abs().rolling(int(n), min_periods=int(n)).mean()
    return (tp - ma) / (0.015 * md.replace(0, np.nan))


def obv(c, v):
    return (np.sign(_s(c).diff().fillna(0)) * _s(v)).cumsum()


def mfi(h, l, c, v, n=14):
    tp = (_s(h) + _s(l) + _s(c)) / 3
    mf = tp * _s(v)
    pos = mf.where(tp > tp.shift(1), 0.0)
    neg = mf.where(tp < tp.shift(1), 0.0)
    mr = pos.rolling(int(n)).sum() / neg.rolling(int(n)).sum().replace(0, np.nan)
    return 100 - 100 / (1 + mr)


def cmf(h, l, c, v, n=20):
    h, l, c, v = _s(h), _s(l), _s(c), _s(v)
    mfm = ((c - l) - (h - c)) / (h - l).replace(0, np.nan)
    return (mfm * v).rolling(int(n)).sum() / v.rolling(int(n)).sum().replace(0, np.nan)


def session_vwap(df, tf_ms):
    tp = (df['high'] + df['low'] + df['close']) / 3
    day = (df['open_time'] // 86_400_000)
    pv = (tp * df['volume']).groupby(day).cumsum()
    vv = df['volume'].groupby(day).cumsum()
    return pv / vv.replace(0, np.nan)


def prior_levels(df, freq='D'):
    """Previous completed period high/low/close mapped to each bar."""
    d = df[['open_time', 'high', 'low', 'close']].copy()
    if freq == 'D':
        key = d['open_time'] // 86_400_000
    else:  # ISO week starting Monday UTC
        key = (d['open_time'] // 86_400_000 + 3) // 7
    g = d.groupby(key)
    agg = g.agg(h=('high', 'max'), l=('low', 'min'), c=('close', 'last'))
    agg = agg.shift(1)
    out = d[['open_time']].copy()
    out['key'] = key
    out = out.merge(agg, left_on='key', right_index=True, how='left')
    return (pd.Series(out['h'].to_numpy(), index=df.index),
            pd.Series(out['l'].to_numpy(), index=df.index),
            pd.Series(out['c'].to_numpy(), index=df.index))


def anchored_vwap(df, anchor_idx):
    tp = (df['high'] + df['low'] + df['close']) / 3
    seg = df.loc[anchor_idx:]
    pv = (tp.loc[anchor_idx:] * seg['volume']).cumsum()
    vv = seg['volume'].cumsum()
    out = pd.Series(np.nan, index=df.index)
    out.loc[anchor_idx:] = (pv / vv.replace(0, np.nan)).to_numpy()
    return out


def ichimoku(h, l, c, t=9, k=26, b=52):
    h, l, c = _s(h), _s(l), _s(c)
    tenkan = (h.rolling(t).max() + l.rolling(t).min()) / 2
    kijun = (h.rolling(k).max() + l.rolling(k).min()) / 2
    a_raw = (tenkan + kijun) / 2
    b_raw = (h.rolling(b).max() + l.rolling(b).min()) / 2
    a_vis = a_raw.shift(k)
    b_vis = b_raw.shift(k)
    return tenkan, kijun, a_raw, b_raw, a_vis, b_vis


def supertrend(h, l, c, n=10, mult=3.0):
    h, l, c = _s(h), _s(l), _s(c)
    a = atr(h, l, c, n)
    mid = (h + l) / 2
    ub = (mid + mult * a).to_numpy(); lb = (mid - mult * a).to_numpy()
    cl = c.to_numpy()
    n_ = len(cl)
    fub = np.full(n_, np.nan); flb = np.full(n_, np.nan); d = np.zeros(n_)
    for i in range(1, n_):
        if np.isnan(ub[i]) or np.isnan(cl[i - 1]):
            continue
        if np.isnan(fub[i - 1]) or np.isnan(flb[i - 1]):
            fub[i], flb[i] = ub[i], lb[i]
            d[i] = 1 if cl[i] > fub[i] else -1
            continue
        fub[i] = ub[i] if (ub[i] < fub[i - 1] or cl[i - 1] > fub[i - 1]) else fub[i - 1]
        flb[i] = lb[i] if (lb[i] > flb[i - 1] or cl[i - 1] < flb[i - 1]) else flb[i - 1]
        if d[i - 1] == 1:
            d[i] = -1 if cl[i] < flb[i] else 1
        else:
            d[i] = 1 if cl[i] > fub[i] else -1
    return pd.Series(d, index=h.index), pd.Series(flb, index=h.index), pd.Series(fub, index=h.index)


def aroon(h, l, n=25):
    n = int(n)
    up = _s(h).rolling(n + 1).apply(lambda a: 100 * (np.argmax(a) / n), raw=True)
    dn = _s(l).rolling(n + 1).apply(lambda a: 100 * (np.argmin(a) / n), raw=True)
    return up, dn


def williams_r(h, l, c, n=14):
    hh = _s(h).rolling(int(n)).max(); ll = _s(l).rolling(int(n)).min()
    return -100 * (hh - _s(c)) / (hh - ll).replace(0, np.nan)


def roc(x, n=10):
    return _s(x) / _s(x).shift(int(n)) - 1


def mom(x, n=10):
    return _s(x) - _s(x).shift(int(n))


def ao(h, l):
    mid = (_s(h) + _s(l)) / 2
    return sma(mid, 5) - sma(mid, 34)


def ac(h, l):
    a = ao(h, l)
    return a - sma(a, 5)


def emv(h, l, v, n=4):
    mid = (_s(h) + _s(l)) / 2
    raw = (mid - mid.shift(1)) * (_s(h) - _s(l)) / _s(v).replace(0, np.nan)
    return ema(raw, n)


def pivot_high(h, left=2, right=2):
    h = _s(h)
    w = int(left) + int(right) + 1
    roll = h.rolling(w, min_periods=w).max()
    is_p = (h.shift(int(right)) >= roll - 1e-12)
    return h.shift(int(right)).where(is_p)


def pivot_low(l, left=2, right=2):
    l = _s(l)
    w = int(left) + int(right) + 1
    roll = l.rolling(w, min_periods=w).min()
    is_p = (l.shift(int(right)) <= roll + 1e-12)
    return l.shift(int(right)).where(is_p)


def last_pivh(h, left=2, right=2):
    return pivot_high(h, left, right).ffill()


def last_pivl(l, left=2, right=2):
    return pivot_low(l, left, right).ffill()


def pivh_age(h, left=2, right=2):
    return bars_since(pivot_high(h, left, right).notna())


def pivl_age(l, left=2, right=2):
    return bars_since(pivot_low(l, left, right).notna())


def heikin_ashi(df):
    o = df['open'].to_numpy(float); h = df['high'].to_numpy(float)
    l = df['low'].to_numpy(float); c = df['close'].to_numpy(float)
    n = len(o)
    ha_c = (o + h + l + c) / 4
    ha_o = np.empty(n); ha_o[0] = (o[0] + c[0]) / 2
    for i in range(1, n):
        ha_o[i] = (ha_o[i - 1] + ha_c[i - 1]) / 2
    ha_h = np.maximum(h, np.maximum(ha_o, ha_c))
    ha_l = np.minimum(l, np.minimum(ha_o, ha_c))
    idx = df.index
    return (pd.Series(ha_o, index=idx), pd.Series(ha_h, index=idx),
            pd.Series(ha_l, index=idx), pd.Series(ha_c, index=idx))


def cpr_levels(df):
    h, l, c = prior_levels(df, 'D')
    p = (h + l + c) / 3
    bc = (h + l) / 2
    tc = 2 * p - bc
    r1 = 2 * p - l
    s1 = 2 * p - h
    r2 = p + (h - l)
    s2 = p - (h - l)
    return p, tc, bc, r1, s1, r2, s2


def ref(x, n):
    return _s(x).shift(int(n))


def _pair(a, b):
    if isinstance(a, pd.Series):
        if not isinstance(b, pd.Series):
            b = pd.Series(b, index=a.index)
    elif isinstance(b, pd.Series):
        a = pd.Series(a, index=b.index)
    else:
        a, b = pd.Series(a), pd.Series(b)
    return a, b


def cross_up(a, b):
    a, b = _pair(a, b)
    return (a > b) & (a.shift(1) <= b.shift(1))


def cross_down(a, b):
    a, b = _pair(a, b)
    return (a < b) & (a.shift(1) >= b.shift(1))


def rising(x, n=1):
    return _s(x) > _s(x).shift(int(n))


def falling(x, n=1):
    return _s(x) < _s(x).shift(int(n))


def highest(x, n):
    return _s(x).rolling(int(n)).max()


def lowest(x, n):
    return _s(x).rolling(int(n)).min()


def std(x, n):
    return _s(x).rolling(int(n)).std(ddof=0)


def count(cond, n):
    return _s(cond).astype(float).rolling(int(n)).sum()


def bars_since(cond):
    cond = _s(cond).fillna(False).astype(int)
    idx = np.arange(len(cond))
    out = pd.Series(np.nan, index=cond.index)
    last = np.nan
    vals = cond.to_numpy()
    for i in range(len(vals)):
        if vals[i]:
            last = i
        out.iloc[i] = i - last if not np.isnan(last) else np.nan
    return out


def between(x, a, b):
    return (_s(x) >= a) & (_s(x) <= b)


def where(cond, a, b):
    return pd.Series(np.where(_s(cond), a, b), index=_s(cond).index)


def shift(x, n):
    return _s(x).shift(int(n))


# ------------------------------------------------------------------------------ DSL
BASE_CTX = dict(sma=sma, ema=ema, rma=rma, wma=wma, lwma=lwma, hma=hma, kama=kama, rsi=rsi,
                atr=atr, adx=adx, macd=macd, bb=bb, donchian=donchian, keltner=keltner,
                stoch=stoch, cci=cci, obv=obv, mfi=mfi, cmf=cmf, ichimoku=ichimoku,
                supertrend=supertrend, aroon=aroon, williams_r=williams_r, roc=roc, mom=mom,
                ao=ao, ac=ac, emv=emv, pivh=pivot_high, pivl=pivot_low, pivot_high=pivot_high,
                pivot_low=pivot_low, last_pivh=last_pivh, last_pivl=last_pivl, pivh_age=pivh_age,
                pivl_age=pivl_age, ref=ref, shift=shift, cross_up=cross_up, cross_down=cross_down,
                rising=rising, falling=falling, highest=highest, lowest=lowest, count=count,
                std=std, bars_since=bars_since, between=between, where=where, abs=np.abs, min=np.minimum,
                max=np.maximum, log=np.log, sqrt=np.sqrt, np=np, pctb=pctb, bbw=bbw)


class _FixPrecedence(ast.NodeTransformer):
    """Re-associate comparisons and bitwise &/| for the DSL.

    Python binds & tighter than comparisons, so `a > b & c > d` is parsed as
    `a > (b & (c > d))`.  In the DSL the intended reading is nearly always
    `(a > b) & (c > d)`.  This transformer rewrites the AST accordingly.
    """

    def visit_Compare(self, node):
        self.generic_visit(node)
        if len(node.ops) != 1:
            return node
        left, right = node.left, node.comparators[0]
        if isinstance(left, ast.BinOp) and isinstance(left.op, (ast.BitAnd, ast.BitOr)):
            new = ast.BinOp(
                left=left.left, op=left.op,
                right=ast.Compare(left=left.right, ops=node.ops, comparators=[right]))
            return ast.copy_location(self.visit(new), node)
        if isinstance(right, ast.BinOp) and isinstance(right.op, (ast.BitAnd, ast.BitOr)):
            new = ast.BinOp(
                left=ast.Compare(left=left, ops=node.ops, comparators=[right.left]),
                op=right.op, right=right.right)
            return ast.copy_location(self.visit(new), node)
        return node


def normalize_expr(expr: str) -> str:
    try:
        cur = expr
        for _ in range(6):
            tree = ast.parse(cur, mode='eval')
            tree = _FixPrecedence().visit(tree)
            ast.fix_missing_locations(tree)
            nxt = ast.unparse(tree)
            if nxt == cur:
                break
            cur = nxt
        return cur
    except Exception:
        return expr


def eval_expr(expr: str, df: pd.DataFrame) -> pd.Series:
    ctx = dict(BASE_CTX)
    for c in ['open', 'high', 'low', 'close', 'volume', 'quote_asset_volume']:
        if c in df:
            ctx[c] = df[c]
    ctx['hl2'] = (df['high'] + df['low']) / 2
    ctx['hlc3'] = (df['high'] + df['low'] + df['close']) / 3
    ctx['ohlc4'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4
    ctx['vwap'] = session_vwap(df, 0)
    pdh, pdl, pdc = prior_levels(df, 'D')
    pwh, pwl, pwc = prior_levels(df, 'W')
    ctx.update(pdh=pdh, pdl=pdl, pdc=pdc, pwh=pwh, pwl=pwl, pwc=pwc)
    daykey = df['open_time'] // 86_400_000
    ctx['day_open'] = df.groupby(daykey)['open'].transform('first')
    ctx['day_high'] = df.groupby(daykey)['high'].transform('cummax')
    ctx['day_low'] = df.groupby(daykey)['low'].transform('cummin')
    ctx['tenkan'], ctx['kijun'], ctx['a_raw'], ctx['b_raw'], ctx['cloud_a'], ctx['cloud_b'] = ichimoku(df['high'], df['low'], df['close'])
    ctx['cloud_up'] = pd.concat([ctx['cloud_a'], ctx['cloud_b']], axis=1).max(axis=1)
    ctx['cloud_lo'] = pd.concat([ctx['cloud_a'], ctx['cloud_b']], axis=1).min(axis=1)
    ctx['cloud_future_up'] = ctx['a_raw'] > ctx['b_raw']
    ctx['chikou_up'] = (df['close'] > df['close'].shift(26)) & (df['close'] > ctx['kijun'].shift(26)) & (df['close'] > ctx['cloud_up'].shift(26))
    ctx['chikou_dn'] = (df['close'] < df['close'].shift(26)) & (df['close'] < ctx['kijun'].shift(26)) & (df['close'] < ctx['cloud_lo'].shift(26))
    ctx['pdi'] = adx(df['high'], df['low'], df['close'])[1]
    ctx['mdi'] = adx(df['high'], df['low'], df['close'])[2]
    ctx['adx14'] = adx(df['high'], df['low'], df['close'])[0]
    ctx['atr14'] = atr(df['high'], df['low'], df['close'], 14)
    ctx['atr20'] = atr(df['high'], df['low'], df['close'], 20)
    ctx['ema20'] = ema(df['close'], 20)
    ctx['sma20'] = sma(df['close'], 20)
    ctx['sma200'] = sma(df['close'], 200)
    ctx['rsi14'] = rsi(df['close'], 14)
    ctx['ha_o'], ctx['ha_h'], ctx['ha_l'], ctx['ha_c'] = heikin_ashi(df)
    ctx['ha_green'] = ctx['ha_c'] > ctx['ha_o']
    ctx['ha_red'] = ctx['ha_c'] < ctx['ha_o']
    pp, tc, bc, r1, s1, r2, s2 = cpr_levels(df)
    ctx.update(pp=pp, cpr_tc=tc, cpr_bc=bc, r1=r1, s1=s1, r2=r2, s2=s2)
    ctx['hour'] = ((df['open_time'] // 3_600_000) % 24).astype(int)
    ctx['minute'] = ((df['open_time'] // 60_000) % 60).astype(int)
    ctx['bar_range'] = df['high'] - df['low']
    out = eval(normalize_expr(expr), {'__builtins__': {}}, ctx)
    if isinstance(out, (bool, np.bool_)):
        out = pd.Series(bool(out), index=df.index)
    return pd.Series(out, index=df.index).fillna(False).astype(bool)


# -------------------------------------------------------------------------- signals
def align_htf(base: pd.DataFrame, htf: pd.DataFrame, expr: str) -> pd.Series:
    """Value of htf expression known at each base bar close (last completed htf bar)."""
    v = eval_expr(expr, htf).astype(float)
    tmp = pd.DataFrame({'t': htf['close_time'].to_numpy(), 'v': v.to_numpy()})
    tmp = tmp.dropna().sort_values('t')
    # base close_time is inclusive; last htf bar whose close_time <= base close_time
    b = pd.DataFrame({'t': base['close_time'].to_numpy()})
    m = pd.merge_asof(b, tmp, on='t', direction='backward')
    return pd.Series(m['v'].to_numpy(), index=base.index)


def build_signals(spec, df, htf_data):
    entry_long = eval_expr(spec['entry_long'], df) if spec.get('entry_long') else pd.Series(False, index=df.index)
    entry_short = eval_expr(spec['entry_short'], df) if spec.get('entry_short') else pd.Series(False, index=df.index)
    ok = pd.Series(True, index=df.index)
    for f in spec.get('filters', []):
        ok &= eval_expr(f, df)
    for hf in spec.get('htf_filters', []):
        htf = htf_data.get(hf['tf'])
        if htf is None or htf.empty:
            ok &= False
        else:
            ok &= align_htf(df, htf, hf['expr']).fillna(False).astype(bool)
    entry_long = entry_long & ok
    entry_short = entry_short & ok
    if spec.get('direction') == 'long':
        entry_short = pd.Series(False, index=df.index)
    if spec.get('direction') == 'short':
        entry_long = pd.Series(False, index=df.index)
    exit_long = eval_expr(spec['exit_long'], df) if spec.get('exit_long') else None
    exit_short = eval_expr(spec['exit_short'], df) if spec.get('exit_short') else None
    return entry_long, entry_short, exit_long, exit_short


# ------------------------------------------------------------------------ execution
def _next_idx(arr, t):
    return int(np.searchsorted(arr, t, side='left'))


def simulate_trade(m1, fund_t, fund_r, sig, side, entry_idx, spec, entry_px=None):
    """Simulate one trade on 1m data. Returns dict or None."""
    ot = m1['open_time']; op = m1['open']; hi = m1['high']; lo = m1['low']; cl = m1['close']
    n1 = len(ot)
    if entry_idx >= n1:
        return None
    entry_time = ot[entry_idx]
    raw_entry = op[entry_idx] if entry_px is None else entry_px
    entry = raw_entry * (1 + SLIP) if side == 1 else raw_entry * (1 - SLIP)

    atr_sig = sig['atr']
    if not np.isfinite(atr_sig) or atr_sig <= 0:
        return None
    stop_mult = spec.get('stop_atr', 2.0)
    tgt_mult = spec.get('target_atr', 0.0)
    rr = spec.get('target_rr', 0.0)
    stop_mode = spec.get('stop_mode', 'atr')
    buf = spec.get('stop_buffer_atr', 0.1)
    if stop_mode == 'signal_low':
        stop = sig['low'] - buf * atr_sig
    elif stop_mode == 'signal_high':
        stop = sig['high'] + buf * atr_sig
    elif stop_mode == 'swing_low':
        stop = sig['swing_low'] - buf * atr_sig
    elif stop_mode == 'swing_high':
        stop = sig['swing_high'] + buf * atr_sig
    else:
        stop_dist = stop_mult * atr_sig
        if spec.get('stop_pct'):
            stop_dist = entry * spec['stop_pct']
        stop = entry - stop_dist if side == 1 else entry + stop_dist
    stop_dist = abs(entry - stop)
    if stop_dist <= 0:
        return None
    if side == 1:
        target = entry + (rr * stop_dist if rr else (tgt_mult * atr_sig if tgt_mult else np.inf))
    else:
        target = entry - (rr * stop_dist if rr else (tgt_mult * atr_sig if tgt_mult else -np.inf))
    if (side == 1 and stop >= entry) or (side == -1 and stop <= entry):
        return None

    time_bars = int(spec.get('time_bars', 0) or 0)
    time_exit_time = sig['close_time'] + time_bars * TF_MS[spec['tf']] if time_bars else None
    trail_mult = spec.get('trail_atr', 0.0)
    be_at_r = spec.get('breakeven_r', 0.0)
    max_bars = int(spec.get('max_hold_bars', 0) or 0)

    exit_idx = None; exit_price = None; reason = None
    # base bar loop, but first the entry minute(s) until next base bar close
    cur_stop = stop
    mfe = 0.0
    j = entry_idx
    # exit signal timestamps are evaluated on base bars; precomputed bool series
    exit_sig = sig.get('exit_signal')
    base_close_times = sig['base_close_times']

    # We iterate base bars after the signal bar. The first base bar end is sig['close_time'] + tf.
    # Then check 1m bars in each window.
    bar_end = sig['close_time'] + TF_MS[spec['tf']]
    base_i = sig['i'] + 1
    while j < n1:
        window_end = min(bar_end, ot[-1] + 60_000)
        # stop/target within [j, window_end)
        k = j
        while k < n1 and ot[k] < window_end:
            o, h, l, c = op[k], hi[k], lo[k], cl[k]
            if side == 1:
                mfe = max(mfe, h - entry)
                if o <= cur_stop:
                    exit_idx, exit_price, reason = k, o, 'stop_gap'; break
                if l <= cur_stop:
                    exit_idx, exit_price, reason = k, cur_stop, 'stop'; break
                if np.isfinite(target) and o >= target:
                    exit_idx, exit_price, reason = k, o, 'target_gap'; break
                if np.isfinite(target) and h >= target:
                    exit_idx, exit_price, reason = k, target, 'target'; break
            else:
                mfe = max(mfe, entry - l)
                if o >= cur_stop:
                    exit_idx, exit_price, reason = k, o, 'stop_gap'; break
                if h >= cur_stop:
                    exit_idx, exit_price, reason = k, cur_stop, 'stop'; break
                if np.isfinite(target) and o <= target:
                    exit_idx, exit_price, reason = k, o, 'target_gap'; break
                if np.isfinite(target) and l <= target:
                    exit_idx, exit_price, reason = k, target, 'target'; break
            k += 1
        if exit_idx is not None:
            break
        j = k
        # bar closed: update trailing / breakeven / check signal exit / time
        if j >= n1:
            break
        # base bar index that just closed
        if base_i < len(base_close_times):
            bct = base_close_times[base_i]
        else:
            bct = ot[-1]
        if trail_mult:
            a = sig['atr_series'][base_i] if base_i < len(sig['atr_series']) else np.nan
            if np.isfinite(a):
                if side == 1:
                    cur_stop = max(cur_stop, cl[j - 1] - trail_mult * a)
                else:
                    cur_stop = min(cur_stop, cl[j - 1] + trail_mult * a)
        if be_at_r and mfe >= be_at_r * stop_dist:
            cur_stop = max(cur_stop, entry) if side == 1 else min(cur_stop, entry)
        if exit_sig is not None and base_i < len(exit_sig) and bool(exit_sig.iloc[base_i]):
            # exit at first 1m open after this base close
            e = _next_idx(ot, bct + 1)
            if e < n1:
                exit_idx, exit_price, reason = e, op[e], 'signal'
            break
        if time_exit_time is not None and bct >= time_exit_time:
            e = _next_idx(ot, bct + 1)
            if e < n1:
                exit_idx, exit_price, reason = e, op[e], 'time'
            break
        if max_bars and base_i - sig['i'] >= max_bars:
            e = _next_idx(ot, bct + 1)
            if e < n1:
                exit_idx, exit_price, reason = e, op[e], 'time'
            break
        base_i += 1
        bar_end = bct + TF_MS[spec['tf']]
    if exit_idx is None:
        # data ended
        exit_idx = n1 - 1; exit_price = cl[-1]; reason = 'data_end'
    exit_time = ot[exit_idx]
    exit_px = exit_price * (1 - SLIP) if side == 1 else exit_price * (1 + SLIP)
    gross = (exit_px - entry) if side == 1 else (entry - exit_px)
    ret = gross / entry
    fees = FEE * (1 + exit_px / entry)
    # funding
    fsum = 0.0
    if len(fund_t):
        a = np.searchsorted(fund_t, entry_time, side='right')
        b = np.searchsorted(fund_t, exit_time, side='left')
        if b > a:
            fsum = float(np.nansum(fund_r[a:b]))
    funding_cost = fsum if side == 1 else -fsum
    net = ret - fees - funding_cost
    return dict(side=side, entry_time=int(entry_time), exit_time=int(exit_time),
                entry=float(entry), exit=float(exit_px), gross=float(ret), fee=float(fees),
                funding=float(funding_cost), net=float(net), reason=reason,
                bars_held=int(base_i - sig['i']), mfe=float(mfe / entry))


def find_entry(m1, t, side, spec, ref_price, atr_val):
    ot = m1['open_time']; op = m1['open']; hi = m1['high']; lo = m1['low']
    i0 = _next_idx(ot, t + 1)
    if i0 >= len(ot):
        return None, None
    lim = spec.get('limit_entry_pct', 0.0) or 0.0
    lim_atr = spec.get('limit_entry_atr', 0.0) or 0.0
    if not lim and not lim_atr:
        return i0, float(op[i0])
    if side == 1:
        px = ref_price * (1 - lim) - lim_atr * atr_val
    else:
        px = ref_price * (1 + lim) + lim_atr * atr_val
    win = int(spec.get('limit_window_bars', 1) or 1)
    end_t = t + win * TF_MS[spec['tf']]
    i = i0
    while i < len(ot) and ot[i] < end_t:
        if side == 1 and lo[i] <= px:
            return i, float(min(op[i], px))
        if side == -1 and hi[i] >= px:
            return i, float(max(op[i], px))
        i += 1
    return None, None


def run_strategy(spec, sym_data, htf_cache=None, max_trades=None):
    """sym_data: dict with tf frames and m1/funding. Returns list of trades."""
    sym = sym_data['symbol']
    tf = spec['tf']
    df = sym_data['tf'].get(tf)
    if df is None or len(df) < 60:
        return []
    m1 = sym_data['m1']
    if not m1:
        return []
    try:
        el, es, xl, xs = build_signals(spec, df, sym_data['htf'])
    except Exception as e:
        return [{'error': f'{sym}: {e}'}]
    atr_series = atr(df['high'], df['low'], df['close'], int(spec.get('atr_n', 14))).to_numpy()
    close_time = df['close_time'].to_numpy()
    close_arr = df['close'].to_numpy()
    low_arr = df['low'].to_numpy()
    high_arr = df['high'].to_numpy()
    sl_n = int(spec.get('swing_lookback', 10) or 10)
    swing_low = pd.Series(low_arr).rolling(sl_n).min().shift(1).to_numpy()
    swing_high = pd.Series(high_arr).rolling(sl_n).max().shift(1).to_numpy()
    trades = []
    last_exit = -1
    # iterate signals chronologically
    for i in range(len(df)):
        if i <= last_exit:
            continue
        long_sig = bool(el.iloc[i]); short_sig = bool(es.iloc[i])
        if not long_sig and not short_sig:
            continue
        # require ATR
        if not np.isfinite(atr_series[i]) or atr_series[i] <= 0:
            continue
        side = 1 if long_sig else -1
        ref = float(close_arr[i])
        e, raw_entry = find_entry(m1, int(close_time[i]), side, spec, ref, float(atr_series[i]))
        if e is None:
            continue
        sig = dict(i=i, close_time=int(close_time[i]), base_close_times=close_time,
                   atr=float(atr_series[i]), atr_series=atr_series,
                   low=float(low_arr[i]), high=float(high_arr[i]),
                   swing_low=float(swing_low[i]) if np.isfinite(swing_low[i]) else float(low_arr[i]),
                   swing_high=float(swing_high[i]) if np.isfinite(swing_high[i]) else float(high_arr[i]),
                   exit_signal=(xl if side == 1 else xs))
        tr = simulate_trade(m1, sym_data['fund_t'], sym_data['fund_r'], sig, side, e, spec, raw_entry)
        if tr is None:
            continue
        tr['symbol'] = sym
        trades.append(tr)
        # convert exit time back to base index for non-overlap
        last_exit = int(np.searchsorted(close_time, tr['exit_time'], side='right') - 1)
        if max_trades and len(trades) >= max_trades:
            break
    return trades


def prepare_symbol(sym, tfs=('5m', '15m', '1h', '4h', '1d'), load_minute=True):
    d = {'symbol': sym, 'tf': {}, 'htf': {}}
    for tf in tfs:
        df = load_tf(sym, tf)
        if not df.empty:
            d['tf'][tf] = df
            d['htf'][tf] = df
    if '1d' in d['tf']:
        w = resample_weekly(d['tf']['1d'])
        if not w.empty:
            d['tf']['1w'] = w
            d['htf']['1w'] = w
    if load_minute:
        d['m1'] = load_1m(sym)
        d['fund_t'], d['fund_r'] = load_funding(sym)
    return d


def metrics(trades):
    if not trades:
        return {}
    r = np.array([t['net'] for t in trades], dtype=float)
    g = np.array([t['gross'] for t in trades], dtype=float)
    wins = r[r > 0]; losses = r[r <= 0]
    eq = np.cumsum(r)
    dd = np.maximum.accumulate(eq) - eq
    return {
        'trades': int(len(r)),
        'win_rate': float(len(wins) / len(r)),
        'avg_net': float(np.mean(r)),
        'median_net': float(np.median(r)),
        'std_net': float(np.std(r)),
        'profit_factor': float(wins.sum() / abs(losses.sum())) if len(losses) and losses.sum() != 0 else None,
        'expectancy': float(np.mean(r)),
        'sharpe_trade': float(np.mean(r) / np.std(r)) if np.std(r) > 0 else None,
        'total_net': float(np.sum(r)),
        'max_dd': float(dd.max()) if len(dd) else 0.0,
        'avg_gross': float(np.mean(g)),
        'fee_drag': float(np.mean(g - r)),
        'avg_hold_h': float(np.mean([(t['exit_time'] - t['entry_time']) / 3.6e6 for t in trades])),
        'long_n': int(sum(1 for t in trades if t['side'] == 1)),
        'short_n': int(sum(1 for t in trades if t['side'] == -1)),
        'symbols': int(len({t['symbol'] for t in trades})),
        'best': float(np.max(r)), 'worst': float(np.min(r)),
    }
