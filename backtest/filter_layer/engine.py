"""Filter-aware strategy execution.

A single price path is simulated per signal. Each filter has its own
non-overlap state, so a trade accepted by filter A can block A's next entry
without affecting filter B. This is exact for each filter individually.

Trade output stores an accepted-mask:
  bits 0..13 = individual filters
  bit 14     = all 14 filters (normally empty because FNG greed/fear conflict)
  bit 15     = baseline (no filter)
"""
from __future__ import annotations
import numpy as np
import pandas as pd
import sys, os

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
sys.path.insert(0, BT)
import bookbt as bt

N_FILTERS = 14
FULL_MASK = (1 << N_FILTERS) - 1
BASE_BIT = 15
ALL_BIT = 14


def build_bar_masks(sym_data, df, daily_mask):
    """Return uint16 condition mask for each strategy bar."""
    close_time = df['close_time'].to_numpy(dtype=np.int64)
    n = len(df)
    m = np.zeros(n, dtype=np.uint16)

    if daily_mask is not None and len(daily_mask):
        ts = daily_mask['ts'].to_numpy(dtype=np.int64)
        # defensive: old files may be seconds; normalise to milliseconds
        if len(ts) and np.nanmax(ts) < 10**12:
            ts = ts * 1000
        vals = daily_mask['mask'].to_numpy(dtype=np.uint16)
        idx = np.searchsorted(ts, close_time, side='right') - 1
        ok = idx >= 0
        m[ok] = vals[idx[ok]]

    vol = pd.to_numeric(df['volume'], errors='coerce').to_numpy(dtype=float)
    med = pd.Series(vol).rolling(20, min_periods=10).median().shift(1).to_numpy(dtype=float)
    surge = np.isfinite(med) & (med > 0) & (vol > 1.5 * med)
    m |= surge.astype(np.uint16) << 11

    ft = sym_data.get('fund_t')
    fr = sym_data.get('fund_r')
    if ft is not None and len(ft):
        fi = np.searchsorted(ft, close_time, side='right') - 1
        fv = np.full(n, np.nan, dtype=float)
        ok = fi >= 0
        fv[ok] = fr[fi[ok]]
        m |= ((fv > 0).astype(np.uint16) << 12)
        m |= ((fv < 0).astype(np.uint16) << 13)
    return m


def run_filtered(spec, sym_data, bar_masks):
    """Run one spec, returning trade dicts with accepted_mask."""
    sym = sym_data['symbol']
    tf = spec['tf']
    df = sym_data['tf'].get(tf)
    if df is None or len(df) < 60:
        return []
    m1 = sym_data.get('m1')
    if not m1:
        return []
    try:
        el, es, xl, xs = bt.build_signals(spec, df, sym_data['htf'])
    except Exception as e:
        return [{'error': f'{sym}: {e}'}]

    atr_series = bt.atr(df['high'], df['low'], df['close'], int(spec.get('atr_n', 14))).to_numpy()
    close_time = df['close_time'].to_numpy(dtype=np.int64)
    close_arr = df['close'].to_numpy(dtype=float)
    low_arr = df['low'].to_numpy(dtype=float)
    high_arr = df['high'].to_numpy(dtype=float)
    sl_n = int(spec.get('swing_lookback', 10) or 10)
    swing_low = pd.Series(low_arr).rolling(sl_n).min().shift(1).to_numpy()
    swing_high = pd.Series(high_arr).rolling(sl_n).max().shift(1).to_numpy()

    last_exit = np.full(N_FILTERS, -1, dtype=np.int64)
    base_last = -1
    all_last = -1
    out = []

    for i in range(len(df)):
        mask = int(bar_masks[i])
        base_free = i > base_last
        passing = [fid for fid in range(N_FILTERS)
                   if ((mask >> fid) & 1) and i > last_exit[fid]]
        all_free = ((mask & FULL_MASK) == FULL_MASK) and (i > all_last)
        if not base_free and not passing and not all_free:
            continue

        long_sig = bool(el.iloc[i])
        short_sig = bool(es.iloc[i])
        if not long_sig and not short_sig:
            continue
        if not np.isfinite(atr_series[i]) or atr_series[i] <= 0:
            continue
        side = 1 if long_sig else -1
        ref = float(close_arr[i])
        e, raw_entry = bt.find_entry(m1, int(close_time[i]), side, spec, ref, float(atr_series[i]))
        if e is None:
            continue
        sig = dict(i=i, close_time=int(close_time[i]), base_close_times=close_time,
                   atr=float(atr_series[i]), atr_series=atr_series,
                   low=float(low_arr[i]), high=float(high_arr[i]),
                   swing_low=float(swing_low[i]) if np.isfinite(swing_low[i]) else float(low_arr[i]),
                   swing_high=float(swing_high[i]) if np.isfinite(swing_high[i]) else float(high_arr[i]),
                   exit_signal=(xl if side == 1 else xs))
        tr = bt.simulate_trade(m1, sym_data['fund_t'], sym_data['fund_r'], sig, side, e, spec, raw_entry)
        if tr is None:
            continue
        exit_idx = int(np.searchsorted(close_time, tr['exit_time'], side='right') - 1)
        accepted = 0
        if base_free:
            accepted |= (1 << BASE_BIT)
            base_last = exit_idx
        for fid in passing:
            accepted |= (1 << fid)
            last_exit[fid] = exit_idx
        if all_free:
            accepted |= (1 << ALL_BIT)
            all_last = exit_idx

        out.append({
            'idx': int(spec['idx']),
            'sid': spec['sid'],
            'tf': tf,
            'symbol': sym,
            'side': int(side),
            'entry_time': int(tr['entry_time']),
            'exit_time': int(tr['exit_time']),
            'net': float(tr['net']),
            'gross': float(tr['gross']),
            'accepted_mask': int(accepted),
            'cond_mask': int(mask),
        })
    return out
