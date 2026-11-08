"""Mechanical strategy families used to translate the book review contracts.

Each builder returns a spec dict consumed by bookbt.run_strategy.
Expressions are evaluated with bookbt.eval_expr (pandas Series semantics,
use & | ~ instead of and/or/not).
"""
from __future__ import annotations


def S(idx, tf, long=None, short=None, stop=2.0, time=14, exit_long=None,
      exit_short=None, direction=None, **kw):
    d = dict(idx=idx, tf=tf, entry_long=long, entry_short=short,
             exit_long=exit_long, exit_short=exit_short,
             stop_atr=stop, time_bars=time, atr_n=kw.pop('atr_n', 14))
    if direction:
        d['direction'] = direction
    elif short:
        d['direction'] = 'both'
    else:
        d['direction'] = 'long'
    d.update(kw)
    return d


def ma_cross(idx, tf='1d', fast=20, slow=50, trend=200, kind='ema', stop=2.0, time=14,
             use_trend=True, long_only=False, short=True):
    f = f'{kind}(close,{fast})'; s = f'{kind}(close,{slow})'
    tr = f'&(close>{kind}(close,{trend}))' if use_trend else ''
    trs = f'&(close<{kind}(close,{trend}))' if use_trend else ''
    L = f'cross_up({f},{s}){tr}'
    Sh = None if long_only or not short else f'cross_down({f},{s}){trs}'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long=f'cross_down({f},{s})', exit_short=(f'cross_up({f},{s})' if Sh else None))


def ma_pullback(idx, tf='1d', fast=20, slow=50, pull=20, lookback=5, stop=2.0, time=14,
                long_only=False, short=True):
    f = f'ema(close,{fast})'; s = f'ema(close,{slow})'; p = f'ema(close,{pull})'
    L = f'({f}>{s})&(close>{s})&rising({s},3)&(ref(count(low<={p},{lookback}),1)>=1)&(close>ref(high,1))'
    Sh = None if long_only or not short else \
        f'({f}<{s})&(close<{s})&falling({s},3)&(ref(count(high>={p},{lookback}),1)>=1)&(close<ref(low,1))'
    return S(idx, tf, L, Sh, stop=stop, time=time, stop_mode='signal_low',
             exit_long=f'close<{p}', exit_short=(f'close>{p}' if Sh else None))


def donchian_break(idx, tf='1d', n=20, trend=200, adx_min=0, vol_mult=0, stop=2.0, time=14,
                   long_only=False, short=True, exit_channel=True):
    L = f'close>ref(highest(high,{n}),1)'
    Sh = None if long_only or not short else f'close<ref(lowest(low,{n}),1)'
    if trend:
        L += f'&(close>sma(close,{trend}))'
        if Sh: Sh += f'&(close<sma(close,{trend}))'
    if adx_min:
        L += f'&(adx14>{adx_min})'
        if Sh: Sh += f'&(adx14>{adx_min})'
    if vol_mult:
        L += f'&(quote_asset_volume>{vol_mult}*ref(sma(quote_asset_volume,20),1))'
        if Sh: Sh += f'&(quote_asset_volume>{vol_mult}*ref(sma(quote_asset_volume,20),1))'
    xl = f'close<ref(lowest(low,{n}),1)' if exit_channel else None
    xs = f'close>ref(highest(high,{n}),1)' if (exit_channel and Sh) else None
    return S(idx, tf, L, Sh, stop=stop, time=time, exit_long=xl, exit_short=xs)


def range_break(idx, tf='1d', n=20, width_atr=4.0, trend=0, stop=2.0, time=14,
                long_only=False, short=True, retest=False):
    U = f'ref(highest(high,{n}),1)'; Lo = f'ref(lowest(low,{n}),1)'
    tight = f'(({U}-{Lo})<={width_atr}*atr14)'
    L = f'{tight}&(close>{U})'
    Sh = None if long_only or not short else f'{tight}&(close<{Lo})'
    if trend:
        L += f'&(close>sma(close,{trend}))'
        if Sh: Sh += f'&(close<sma(close,{trend}))'
    if retest:
        L = f'{tight}&(ref(close,1)>{U})&(low<={U})&(close>{U})'
        if Sh: Sh = f'{tight}&(ref(close,1)<{Lo})&(high>={Lo})&(close<{Lo})'
    return S(idx, tf, L, Sh, stop=stop, time=time, exit_long=f'close<{Lo}', exit_short=(f'close>{U}' if Sh else None))


def pivot_break(idx, tf='1d', left=2, right=2, trend=20, stop=2.0, time=14,
                long_only=False, short=True):
    ph = f'ref(last_pivh(high,{left},{right}),1)'; pl = f'ref(last_pivl(low,{left},{right}),1)'
    L = f'(close>{ph})&(close>ema(close,{trend}))&(pdi>mdi)'
    Sh = None if long_only or not short else f'(close<{pl})&(close<ema(close,{trend}))&(mdi>pdi)'
    return S(idx, tf, L, Sh, stop=stop, time=time, stop_mode='signal_low')


def bb_reversion(idx, tf='1d', n=20, k=2.0, rsi_n=14, low=30, high=70, trend=0,
                 stop=2.0, time=14, long_only=False, short=True):
    lo = f'bb(close,{n},{k})[2]'; up = f'bb(close,{n},{k})[1]'; mid = f'bb(close,{n},{k})[0]'
    L = f'(ref(close,1)<ref({lo},1))&(close>{lo})&(ref(rsi(close,{rsi_n}),1)<{low})'
    Sh = None if long_only or not short else f'(ref(close,1)>{up})&(close<{up})&(ref(rsi(close,{rsi_n}),1)>{high})'
    if trend:
        L += f'&(close>sma(close,{trend}))'
        if Sh: Sh += f'&(close<sma(close,{trend}))'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long=f'close>{mid}', exit_short=(f'close<{mid}' if Sh else None))


def bb_break(idx, tf='1d', n=20, k=2.0, trend=200, stop=2.0, time=14,
             long_only=False, short=True):
    L = f'(close>bb(close,{n},{k})[1])&(bb(close,{n},{k})[1]>ref(bb(close,{n},{k})[1],1))'
    Sh = None if long_only or not short else f'(close<bb(close,{n},{k})[2])&(bb(close,{n},{k})[2]<ref(bb(close,{n},{k})[2],1))'
    if trend:
        L += f'&(close>sma(close,{trend}))'
        if Sh: Sh += f'&(close<sma(close,{trend}))'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long=f'close<bb(close,{n},{k})[0]', exit_short=(f'close>bb(close,{n},{k})[0]' if Sh else None))


def rsi_reversion(idx, tf='1d', n=14, low=30, high=70, exit_level=50, trend=0,
                  stop=2.0, time=14, long_only=False, short=True):
    L = f'(ref(rsi(close,{n}),1)<{low})&(rsi(close,{n})>={low})'
    Sh = None if long_only or not short else f'(ref(rsi(close,{n}),1)>{high})&(rsi(close,{n})<={high})'
    if trend:
        L += f'&(close>sma(close,{trend}))'
        if Sh: Sh += f'&(close<sma(close,{trend}))'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long=f'rsi(close,{n})>{exit_level}', exit_short=(f'rsi(close,{n})<{100-exit_level}' if Sh else None))


def rsi_momentum(idx, tf='1d', n=14, level=50, stop=2.0, time=14, long_only=False, short=True):
    L = f'(ref(rsi(close,{n}),1)<={level})&(rsi(close,{n})>{level})'
    Sh = None if long_only or not short else f'(ref(rsi(close,{n}),1)>={100-level})&(rsi(close,{n})<{100-level})'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long=f'rsi(close,{n})<{level}', exit_short=(f'rsi(close,{n})>{100-level}' if Sh else None))


def macd_cross(idx, tf='1d', fast=12, slow=26, sig=9, zero_filter=False, stop=2.0, time=14,
               long_only=False, short=True):
    line = f'macd(close,{fast},{slow},{sig})[0]'; sg = f'macd(close,{fast},{slow},{sig})[1]'
    L = f'cross_up({line},{sg})'
    Sh = None if long_only or not short else f'cross_down({line},{sg})'
    if zero_filter:
        L += f'&({line}>0)'
        if Sh: Sh += f'&({line}<0)'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long=f'cross_down({line},{sg})', exit_short=(f'cross_up({line},{sg})' if Sh else None))


def macd_hist(idx, tf='1d', fast=12, slow=26, sig=9, stop=2.0, time=14,
              long_only=False, short=True):
    h = f'macd(close,{fast},{slow},{sig})[2]'
    L = f'(ref({h},1)<=0)&({h}>0)'
    Sh = None if long_only or not short else f'(ref({h},1)>=0)&({h}<0)'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long=f'{h}<0', exit_short=(f'{h}>0' if Sh else None))


def stoch(idx, tf='1h', k=14, d=3, smooth=3, low=20, high=80, stop=2.0, time=14,
          long_only=False, short=True):
    K = f'stoch(high,low,close,{k},{d},{smooth})[0]'; D = f'stoch(high,low,close,{k},{d},{smooth})[1]'
    L = f'(ref({K},1)<={D})&({K}>{D})&({K}<{low+15})'
    Sh = None if long_only or not short else f'(ref({K},1)>={D})&({K}<{D})&({K}>{high-15})'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long=f'cross_down({K},{D})', exit_short=(f'cross_up({K},{D})' if Sh else None))


def ichimoku_cloud(idx, tf='1d', stop=2.0, time=14, long_only=False, short=True):
    L = f'(ref(close,1)<=ref(cloud_up,1))&(close>cloud_up)&(tenkan>kijun)'
    Sh = None if long_only or not short else f'(ref(close,1)>=ref(cloud_lo,1))&(close<cloud_lo)&(tenkan<kijun)'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long='close<kijun', exit_short=('close>kijun' if Sh else None))


def ichimoku_tk(idx, tf='1d', cloud_filter=True, stop=2.0, time=14, long_only=False, short=True):
    L = 'cross_up(tenkan,kijun)'
    Sh = None if long_only or not short else 'cross_down(tenkan,kijun)'
    if cloud_filter:
        L += '&(close>cloud_up)'
        if Sh: Sh += '&(close<cloud_lo)'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long='cross_down(tenkan,kijun)', exit_short=('cross_up(tenkan,kijun)' if Sh else None))


def supertrend_flip(idx, tf='4h', n=10, mult=3.0, stop=2.0, time=30, long_only=False, short=True):
    L = 'cross_up(supertrend(high,low,close,%d,%s)[0],0)' % (n, mult)
    Sh = None if long_only or not short else 'cross_down(supertrend(high,low,close,%d,%s)[0],0)' % (n, mult)
    return S(idx, tf, L, Sh, stop=stop, time=time)


def keltner_rev(idx, tf='1h', n=20, mult=1.5, rsi_n=5, low=30, high=70, stop=2.0, time=14,
                long_only=False, short=True):
    lo = f'keltner(close,high,low,{n},{mult})[2]'; up = f'keltner(close,high,low,{n},{mult})[1]'
    L = f'(low<={lo})&(close>{lo})&(ref(rsi(close,{rsi_n}),1)<{low})'
    Sh = None if long_only or not short else f'(high>={up})&(close<{up})&(ref(rsi(close,{rsi_n}),1)>{high})'
    return S(idx, tf, L, Sh, stop=stop, time=time)


def cci_rev(idx, tf='1d', n=20, low=-200, high=200, exit_level=0, stop=2.0, time=14,
            long_only=False, short=True):
    c = f'cci(high,low,close,{n})'
    L = f'(ref({c},1)<{low})&({c}>{low})'
    Sh = None if long_only or not short else f'(ref({c},1)>{high})&({c}<{high})'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long=f'{c}>{exit_level}', exit_short=(f'{c}<{exit_level}' if Sh else None))


def vwap_rev(idx, tf='15m', k=2.0, stop=2.0, time=32, long_only=False, short=True):
    L = f'(close<vwap-{k}*atr14)&(close>ref(close,1))'
    Sh = None if long_only or not short else f'(close>vwap+{k}*atr14)&(close<ref(close,1))'
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long='close>=vwap', exit_short=('close<=vwap' if Sh else None))


def vwap_break(idx, tf='15m', stop=2.0, time=32, long_only=False, short=True):
    L = '(ref(close,1)<=ref(vwap,1))&(close>vwap)&(volume>ref(sma(volume,20),1))'
    Sh = None if long_only or not short else '(ref(close,1)>=ref(vwap,1))&(close<vwap)&(volume>ref(sma(volume,20),1))'
    return S(idx, tf, L, Sh, stop=stop, time=time, exit_long='close<vwap', exit_short=('close>vwap' if Sh else None))


def double_pattern(idx, tf='1d', look=10, tol=0.5, stop=2.0, time=14, long_only=False, short=True):
    # neckline break after two lows/highs within tol*ATR
    L = (f'(close>ref(highest(high,{look}),1))&'
         f'(abs(lowest(low,{look})-ref(lowest(low,{look}),{look}))<{tol}*atr14)')
    Sh = None if long_only or not short else \
        (f'(close<ref(lowest(low,{look}),1))&'
         f'(abs(highest(high,{look})-ref(highest(high,{look}),{look}))<{tol}*atr14)')
    return S(idx, tf, L, Sh, stop=stop, time=time, stop_mode='signal_low')


def fib_retrace(idx, tf='1h', look=2, low=0.5, high=0.618, trend=200, stop=2.0, time=48,
                long_only=False, short=True):
    H = f'last_pivh(high,{look},{look})'; Lo = f'last_pivl(low,{look},{look})'
    lvl = f'({H}-{high}*({H}-{Lo}))'
    L = f'(close>ema(close,{trend}))&(low<={lvl})&(close>{lvl})'
    lvl_s = f'({Lo}+{high}*({H}-{Lo}))'
    Sh = None if long_only or not short else f'(close<ema(close,{trend}))&(high>={lvl_s})&(close<{lvl_s})'
    return S(idx, tf, L, Sh, stop=stop, time=time)


def candle_pattern(idx, tf='1d', kind='engulf', trend=0, stop=2.0, time=14,
                   long_only=False, short=True):
    if kind == 'engulf':
        L = '(close>open)&(ref(close,1)<ref(open,1))&(close>=ref(open,1))&(open<=ref(close,1))'
        Sh = None if long_only or not short else '(close<open)&(ref(close,1)>ref(open,1))&(close<=ref(open,1))&(open>=ref(close,1))'
    elif kind == 'pin':
        L = '((min(open,close)-low)>=2*abs(close-open))&((high-max(open,close))<=0.35*(high-low))&(close>open)'
        Sh = None if long_only or not short else '((high-max(open,close))>=2*abs(close-open))&((min(open,close)-low)<=0.35*(high-low))&(close<open)'
    elif kind == 'inside':
        L = '(ref(high,1)<ref(high,2))&(ref(low,1)>ref(low,2))&(close>ref(high,1))'
        Sh = None if long_only or not short else '(ref(high,1)<ref(high,2))&(ref(low,1)>ref(low,2))&(close<ref(low,1))'
    else:
        L = 'close>open'; Sh = None
    if trend:
        L += f'&(close>ema(close,{trend}))'
        if Sh: Sh += f'&(close<ema(close,{trend}))'
    return S(idx, tf, L, Sh, stop=stop, time=time, stop_mode='signal_low')


def session_level(idx, tf='1h', mode='break', stop=2.0, time=24, long_only=False, short=True):
    if mode == 'break':
        L = '(close>pdh)&(ref(close,1)<=ref(pdh,1))'
        Sh = None if long_only or not short else '(close<pdl)&(ref(close,1)>=ref(pdl,1))'
    elif mode == 'failed':
        L = '(high>pdh)&(close<pdh)'
        Sh = None if long_only or not short else '(low<pdl)&(close>pdl)'
    else:  # sweep of prior level and reclaim
        L = '(low<pdl)&(close>pdl)'
        Sh = None if long_only or not short else '(high>pdh)&(close<pdh)'
    return S(idx, tf, L, Sh, stop=stop, time=time)


def donchian_std(idx, tf='1d', n=20, std_n=30, mult=0.5, stop=2.0, time=14,
                 long_only=False, short=True):
    buf = f'{mult}*std(close,{std_n})'
    L = f'close>ref(highest(high,{n}),1)+{buf}'
    Sh = None if long_only or not short else f'close<ref(lowest(low,{n}),1)-{buf}'
    return S(idx, tf, L, Sh, stop=stop, time=time)


def adx_break(idx, tf='1d', n=20, adx_max=20, stop=2.0, time=14, long_only=False, short=True):
    L = f'(ref(adx14,1)<{adx_max})&(close>ref(highest(high,{n}),1))'
    Sh = None if long_only or not short else f'(ref(adx14,1)<{adx_max})&(close<ref(lowest(low,{n}),1))'
    return S(idx, tf, L, Sh, stop=stop, time=time)


def range_mid(idx, tf='1d', n=20, stop=2.0, time=14, long_only=False, short=True):
    mid = f'((highest(high,{n})+lowest(low,{n}))/2)'
    L = f'(ref(close,1)<ref({mid},1))&(close>{mid})'
    Sh = None if long_only or not short else f'(ref(close,1)>{mid})&(close<{mid})'
    return S(idx, tf, L, Sh, stop=stop, time=time)


def nr_break(idx, tf='1d', n=4, stop=2.0, time=14, long_only=False, short=True):
    rng = '(high-low)'
    L = f'(ref({rng},1)<=ref(lowest({rng},{n}),2))&(close>ref(high,1))'
    Sh = None if long_only or not short else f'(ref({rng},1)<=ref(lowest({rng},{n}),2))&(close<ref(low,1))'
    return S(idx, tf, L, Sh, stop=stop, time=time)


def smma_channel(idx, tf='1d', n=55, wr=55, stoch_n=5, stop=2.0, time=14,
                 long_only=False, short=True):
    L = (f'(close>rma(high,{n}))&(williams_r(high,low,close,{wr})>-50)'
         f'&(stoch(high,low,close,{stoch_n},{stoch_n},{stoch_n})[0]'
         f'>stoch(high,low,close,{stoch_n},{stoch_n},{stoch_n})[1])')
    Sh = None if long_only or not short else \
        (f'(close<rma(low,{n}))&(williams_r(high,low,close,{wr})<-50)'
         f'&(stoch(high,low,close,{stoch_n},{stoch_n},{stoch_n})[0]'
         f'<stoch(high,low,close,{stoch_n},{stoch_n},{stoch_n})[1])')
    return S(idx, tf, L, Sh, stop=stop, time=time,
             exit_long=f'close<rma(low,{n})', exit_short=(f'close>rma(high,{n})' if Sh else None))


def ha_reversal(idx, tf='1d', stop=2.0, time=14, long_only=False, short=True):
    L = '(ref(ha_red,1))&(ref(ha_red,2))&(ha_green)&(ref(ha_green,1))'
    Sh = None if long_only or not short else '(ref(ha_green,1))&(ref(ha_green,2))&(ha_red)&(ref(ha_red,1))'
    return S(idx, tf, L, Sh, stop=stop, time=time)


def td_setup(idx, tf='1d', n=9, stop=2.0, time=14, long_only=False, short=True):
    L = f'(ref(count(close<ref(close,4),{n}),1)>={n})&(close>ref(high,1))'
    Sh = None if long_only or not short else f'(ref(count(close>ref(close,4),{n}),1)>={n})&(close<ref(low,1))'
    return S(idx, tf, L, Sh, stop=stop, time=time)


def pivot_point(idx, tf='1h', level='pp', stop=2.0, time=24, long_only=False, short=True):
    L = f'(ref(close,1)<={level})&(close>{level})'
    Sh = None if long_only or not short else f'(ref(close,1)>={level})&(close<{level})'
    return S(idx, tf, L, Sh, stop=stop, time=time)


def cpr_break(idx, tf='5m', stop=2.0, time=48, long_only=False, short=True):
    L = '(ref(close,1)<=ref(max(cpr_tc,cpr_bc),1))&(close>max(cpr_tc,cpr_bc))'
    Sh = None if long_only or not short else '(ref(close,1)>=ref(min(cpr_tc,cpr_bc),1))&(close<min(cpr_tc,cpr_bc))'
    return S(idx, tf, L, Sh, stop=stop, time=time)


def three_methods(idx, tf='1d', stop=2.0, time=14, long_only=False, short=True):
    L = ('(close>ref(close,4))&(ref(count(abs(close-open)<0.5*ref(atr14,1),3),1)>=3)'
         '&(ref(close,1)>ref(open,1))&(close>ref(high,1))')
    Sh = None if long_only or not short else \
        ('(close<ref(close,4))&(ref(count(abs(close-open)<0.5*ref(atr14,1),3),1)>=3)'
         '&(ref(close,1)<ref(open,1))&(close<ref(low,1))')
    return S(idx, tf, L, Sh, stop=stop, time=time)
