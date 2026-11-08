import os, sys, json, glob, re, math, hashlib
import numpy as np
import pandas as pd

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
ROOT = r'D:\Paper_ML_BSH\analysis\book_signal_review'
sys.path.insert(0, BT)
import bookbt as bt

OUT = os.path.join(BT, os.environ.get('BOOKBT_RESULTS', 'results'))
N_SYMBOLS = int(os.environ.get('BOOKBT_N_SYMBOLS', '58'))
DATA_OUT = os.path.join(BT, os.environ.get('BOOKBT_DATA', 'dashboard_data.json'))
CSV_OUT = os.path.join(BT, os.environ.get('BOOKBT_CSV', 'strategy_metrics.csv'))
CONF = ('high', 'medium')


def load_specs():
    specs = json.load(open(os.path.join(BT, 'specs_final.json'), encoding='utf-8'))
    return {s['idx']: s for s in specs}


def load_summaries():
    files = glob.glob(os.path.join(OUT, 'summary', '*.parquet'))
    if not files:
        return pd.DataFrame()
    return pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)


def load_monthly():
    files = glob.glob(os.path.join(OUT, 'monthly', '*.parquet'))
    if not files:
        return pd.DataFrame()
    return pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)


def aggregate_specs(specs, summary, monthly):
    rows = []
    monthly_map = {}
    if not monthly.empty:
        monthly['month'] = pd.to_datetime(monthly['month'] + '-01', utc=True)
        for idx, g in monthly.groupby('idx'):
            g = g.groupby('month')[['pnl', 'pnl_simple', 'n']].sum().sort_index()
            if g.empty:
                continue
            full = pd.date_range(g.index.min(), g.index.max(), freq='MS', tz='UTC')
            g = g.reindex(full, fill_value=0.0)
            eq = (1.0 + g['pnl']).cumprod()
            peak = np.maximum.accumulate(eq.to_numpy())
            dd = float((eq.to_numpy() / peak - 1.0).min()) if len(eq) else 0.0
            sd = float(g['pnl'].std(ddof=1)) if len(g) > 1 else 0.0
            sharpe = float(g['pnl'].mean() / sd * math.sqrt(12)) if sd > 0 else 0.0
            yearly = {}
            for y, gy in g.groupby(g.index.year):
                yearly[str(y)] = float((1.0 + gy['pnl']).prod() - 1.0)
            monthly_map[idx] = {
                'months': [d.strftime('%Y-%m') for d in g.index],
                'pnl': [round(float(x), 6) for x in g['pnl'].to_numpy()],
                'equity': [round(float(x), 6) for x in eq.to_numpy()],
                'max_dd': dd,
                'sharpe': sharpe,
                'yearly': yearly,
            }
    for idx, g in summary.groupby('idx'):
        s = specs.get(int(idx))
        if s is None:
            continue
        n = int(g['n'].sum())
        if n <= 0:
            continue
        w = g['n'].to_numpy(float)
        avg_net = float(np.average(g['avg_net'].to_numpy(float), weights=w))
        win_rate = float(np.average(g['win_rate'].to_numpy(float), weights=w))
        total_net = float(g['total_net'].sum())
        fee_sum = float(g['fee_sum'].sum())
        funding_sum = float(g['funding_sum'].sum())
        gross_total = total_net + fee_sum + funding_sum
        gp = float(g['gross_profit'].sum())
        gl = float(g['gross_loss'].sum())
        sym_avg = g['avg_net'].to_numpy(float)
        abs_total = g['total_net'].abs().to_numpy(float)
        mm = monthly_map.get(int(idx), {})
        row = {
            'idx': int(idx), 'sid': s['sid'], 'batch': s['batch'], 'title': s['title'],
            'family': s['family'], 'tf': s['tf'], 'confidence': s.get('confidence', ''),
            'status': s.get('status', ''),
            'summary': s.get('summary', ''),
            'rule_long': s.get('entry_long') or '',
            'rule_short': s.get('entry_short') or '',
            'n': n, 'symbols': int(g['symbol'].nunique()),
            'avg_net': avg_net, 'median_net': float(np.average(g['median_net'].to_numpy(float), weights=w)),
            'median_symbol_net': float(np.median(sym_avg)),
            'pct_symbols_positive': float((sym_avg > 0).mean()),
            'max_symbol_avg_net': float(sym_avg.max()),
            'concentration': float(abs_total.max() / max(abs_total.sum(), 1e-9)),
            'top_symbol': str(g.loc[g['total_net'].idxmax(), 'symbol']),
            'worst_symbol': str(g.loc[g['total_net'].idxmin(), 'symbol']),
            'total_net': total_net, 'gross_total': gross_total,
            'avg_gross': gross_total / n,
            'fee_sum': fee_sum, 'funding_sum': funding_sum,
            'fee_drag': (fee_sum + funding_sum) / n,
            'win_rate': win_rate,
            'profit_factor': gp / gl if gl > 0 else (999.0 if gp > 0 else 0.0),
            'gross_profit': gp, 'gross_loss': gl,
            'long_n': int(g['long_n'].sum()), 'short_n': int(g['short_n'].sum()),
            'long_net': float(g['long_net'].sum()), 'short_net': float(g['short_net'].sum()),
            'avg_hold_h': float(np.average(g['avg_hold_h'].to_numpy(float), weights=w)),
            'first_entry': int(g['first_entry'].min()), 'last_exit': int(g['last_exit'].max()),
            'years': float(max((g['last_exit'].max() - g['first_entry'].min()) / (365.25 * 24 * 3600 * 1000), 1 / 365.25)),
            'portfolio_net': mm.get('equity', [1.0])[-1] - 1.0 if mm.get('equity') else 0.0,
            'max_dd': mm.get('max_dd', 0.0),
            'sharpe': mm.get('sharpe', 0.0),
            'yearly': mm.get('yearly', {}),
            'monthly': mm.get('months', []),
            'monthly_pnl': mm.get('pnl', []),
            'monthly_equity': mm.get('equity', []),
        }
        row['trades_per_month'] = n / max(row['years'] * 12, 1)
        rows.append(row)
    return sorted(rows, key=lambda x: x['portfolio_net'], reverse=True)


def benchmark():
    syms = bt.symbols()
    btc = bt.load_tf('BTCUSDT', '1d')
    btc = btc[(bt.pd.to_datetime(btc['ts'], utc=True) >= pd.Timestamp('2022-08-01', tz='UTC')) &
              (bt.pd.to_datetime(btc['ts'], utc=True) <= pd.Timestamp('2026-08-31 23:59:59', tz='UTC'))]
    btc_ret = float(btc['close'].iloc[-1] / btc['close'].iloc[0] - 1) if len(btc) > 1 else 0.0
    # monthly equal-weight basket
    rets = []
    for sym in syms:
        df = bt.load_tf(sym, '1d')
        if len(df) < 30:
            continue
        s = df.set_index(pd.to_datetime(df['ts'], utc=True))['close'].resample('ME').last()
        r = s.pct_change()
        r.name = sym
        rets.append(r)
    if rets:
        R = pd.concat(rets, axis=1)
        R = R[(R.index >= pd.Timestamp('2022-08-31', tz='UTC')) & (R.index <= pd.Timestamp('2026-08-31', tz='UTC'))]
        ew = R.mean(axis=1, skipna=True).dropna()
        basket = float((1.0 + ew).prod() - 1.0)
        basket_months = [d.strftime('%Y-%m') for d in ew.index]
        basket_pnl = [round(float(x), 6) for x in ew.to_numpy()]
    else:
        basket, basket_months, basket_pnl = 0.0, [], []
    btc_m = btc.set_index(pd.to_datetime(btc['ts'], utc=True))['close'].resample('ME').last().pct_change().dropna()
    btc_m = btc_m[(btc_m.index >= pd.Timestamp('2022-08-31', tz='UTC')) & (btc_m.index <= pd.Timestamp('2026-08-31', tz='UTC'))]
    return {
        'btc_return': btc_ret,
        'btc_months': [d.strftime('%Y-%m') for d in btc_m.index],
        'btc_pnl': [round(float(x), 6) for x in btc_m.to_numpy()],
        'basket_return': basket,
        'basket_months': basket_months,
        'basket_pnl': basket_pnl,
        'start': '2022-08-01', 'end': '2026-08-31',
    }


def batch_coverage(specs, agg):
    secs = json.load(open(os.path.join(BT, 'sections.json'), encoding='utf-8'))
    batches = sorted(d for d in os.listdir(ROOT) if re.fullmatch(r'batch_\d{3}', d))
    by = {}
    for s in specs.values():
        by.setdefault(s['batch'], []).append(s)
    best_by_batch = {}
    for r in agg:
        b = r['batch']
        if r['n'] >= 20 and r['symbols'] >= 5:
            score = (r.get('median_symbol_net', -1), r['portfolio_net'])
            if b not in best_by_batch or score > best_by_batch[b][0]:
                best_by_batch[b] = (score, r)
    out = []
    for b in batches:
        ss = by.get(b, [])
        tested = [s for s in ss if s['status'] == 'tested' and s.get('confidence') in CONF]
        low = [s for s in ss if s['status'] == 'tested' and s.get('confidence') == 'low']
        exc = [s for s in ss if s['status'] == 'excluded']
        if not ss:
            status = 'no_sections'
        elif tested:
            status = 'tested'
        elif low:
            status = 'low_only'
        else:
            status = 'excluded_only'
        best = best_by_batch.get(b, (None, None))[1]
        out.append({
            'batch': b,
            'sections': len(ss),
            'tested': len(tested),
            'low': len(low),
            'excluded': len(exc),
            'status': status,
            'best_sid': best['sid'] if best else '',
            'best_title': best['title'] if best else '',
            'best_tf': best['tf'] if best else '',
            'best_is_duplicate': bool(best.get('is_duplicate', False)) if best else False,
            'best_rule_lead': best.get('rule_group_lead', '') if best else '',
            'best_portfolio_net': round(best['portfolio_net'], 6) if best else None,
            'best_avg_net': round(best['avg_net'], 6) if best else None,
            'best_median_symbol_net': round(best.get('median_symbol_net', 0), 6) if best else None,
            'best_pct_symbols_positive': round(best.get('pct_symbols_positive', 0), 6) if best else None,
            'best_n': best['n'] if best else 0,
            'reasons': sorted(set(s.get('reason', '') for s in exc if s.get('reason')))[:3],
        })
    return out


def main():
    specs = load_specs()
    summary = load_summaries()
    monthly = load_monthly()
    print('summary rows', len(summary), 'monthly rows', len(monthly), flush=True)
    agg = aggregate_specs(specs, summary, monthly)
    # group identical mechanical rules (same TF, family, expressions, stop/time)
    def _k(x):
        return '' if x is None else str(x)
    tested = [s for s in specs.values() if s.get('status') == 'tested' and s.get('confidence') in CONF]
    groups = {}
    for s in tested:
        key_src = f"{s['tf']}|{s['family']}|{_k(s.get('entry_long'))}|{_k(s.get('entry_short'))}|{_k(s.get('stop'))}|{_k(s.get('time'))}"
        key = hashlib.md5(key_src.encode('utf-8')).hexdigest()
        groups.setdefault(key, []).append(s)
    agg_sids = {r['sid'] for r in agg}
    for r in agg:
        sp = specs[r['idx']]
        key_src = f"{r['tf']}|{r['family']}|{_k(r['rule_long'])}|{_k(r['rule_short'])}|{_k(sp.get('stop'))}|{_k(sp.get('time'))}"
        key = hashlib.md5(key_src.encode('utf-8')).hexdigest()
        r['rule_key'] = key
        group = groups.get(key, [sp])
        traded = [s for s in group if s['sid'] in agg_sids]
        lead = min(traded or group, key=lambda x: (x['batch'], x['sid']))
        r['rule_group_size'] = len(group)
        r['rule_group_lead'] = lead['sid']
        r['is_duplicate'] = r['sid'] != lead['sid']
    bench = benchmark()
    batches = batch_coverage(specs, agg)
    # timeframe summary
    tf_rows = []
    for tf, g in pd.DataFrame(agg).groupby('tf'):
        tf_rows.append({
            'tf': tf, 'specs': len(g), 'trades': int(g['n'].sum()), 'symbols': int(g['symbols'].max()),
            'avg_gross': float(g['avg_gross'].mean()),
            'avg_net': float(g['avg_net'].mean()),
            'median_net': float(g['avg_net'].median()),
            'median_symbol_net': float(g['median_symbol_net'].median()),
            'pct_symbols_positive': float(g['pct_symbols_positive'].mean()),
            'median_portfolio': float(g['portfolio_net'].median()),
            'fee_drag': float(g['fee_drag'].mean()),
            'pct_positive': float((g['avg_net'] > 0).mean()),
        })
    tf_rows.sort(key=lambda x: {'5m': 0, '15m': 1, '1h': 2, '4h': 3, '1d': 4, '1w': 5}.get(x['tf'], 9))
    fam_rows = []
    for fam, g in pd.DataFrame(agg).groupby('family'):
        if len(g) < 3:
            continue
        fam_rows.append({
            'family': fam, 'specs': len(g), 'trades': int(g['n'].sum()),
            'avg_net': float(g['avg_net'].mean()),
            'median_net': float(g['avg_net'].median()),
            'median_portfolio': float(g['portfolio_net'].median()),
            'pct_positive': float((g['avg_net'] > 0).mean()),
        })
    fam_rows.sort(key=lambda x: x['median_portfolio'], reverse=True)
    meta = {
        'n_batches': 215, 'n_sections': 454, 'n_symbols': N_SYMBOLS,
        'n_tested_specs': sum(1 for s in specs.values() if s['status'] == 'tested' and s.get('confidence') in CONF),
        'n_unique_rules': len(groups),
        'n_specs_with_trades': len(agg),
        'n_tested_batches': sum(1 for b in batches if b['status'] == 'tested'),
        'n_low_specs': sum(1 for s in specs.values() if s['status'] == 'tested' and s.get('confidence') == 'low'),
        'n_low_batches': sum(1 for b in batches if b['status'] == 'low_only'),
        'n_excluded_sections': sum(1 for s in specs.values() if s['status'] == 'excluded'),
        'n_excluded_batches': sum(1 for b in batches if b['status'] == 'excluded_only'),
        'n_no_sections': sum(1 for b in batches if b['status'] == 'no_sections'),
        'fee_bps': 5.0, 'slip_bps': 2.0,
        'start': '2022-08-01', 'end': '2026-08-31',
        'exec_end': '2026-10-18',
        'n_summary_rows': len(summary),
        'n_monthly_rows': len(monthly),
    }
    data = {'meta': meta, 'specs': agg, 'batches': batches, 'benchmark': bench,
            'tf': tf_rows, 'families': fam_rows}
    json.dump(data, open(DATA_OUT, 'w', encoding='utf-8'),
              ensure_ascii=False)
    pd.DataFrame(agg).drop(columns=['monthly', 'monthly_pnl', 'monthly_equity', 'yearly']).to_csv(
        CSV_OUT, index=False, encoding='utf-8-sig')
    print('specs', len(agg), 'batches', len(batches), 'tf', tf_rows, flush=True)
    print('benchmark', bench['btc_return'], bench['basket_return'], flush=True)


if __name__ == '__main__':
    main()
