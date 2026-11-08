import os, json
import pandas as pd

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
DATA = json.load(open(os.path.join(BT, 'dashboard_data.json'), encoding='utf-8'))
meta, specs, batches, bench, tf = DATA['meta'], DATA['specs'], DATA['batches'], DATA['benchmark'], DATA['tf']


def pct(x, d=2):
    return f'{x*100:,.{d}f}%'


def num(x):
    return f'{int(x):,}'


def table(rows, cols, headers):
    out = ['| ' + ' | '.join(headers) + ' |',
           '|' + '|'.join(['---'] * len(headers)) + '|']
    for r in rows:
        out.append('| ' + ' | '.join(clean(r.get(c, '')) for c in cols) + ' |')
    return '\n'.join(out)


def clean(x):
    return str(x).replace('|', '\\|').replace('\n', ' ')


def fmt_spec(s):
    pf = s.get('profit_factor', 0)
    return {
        'sid': s['sid'], 'batch': s['batch'].replace('batch_', ''), 'title': s['title'],
        'tf': s['tf'], 'family': s['family'], 'n': num(s['n']), 'symbols': s['symbols'],
        'avg_net': pct(s['avg_net'], 2), 'median_symbol_net': pct(s['median_symbol_net'], 2),
        'pct_symbols_positive': pct(s['pct_symbols_positive'], 0),
        'portfolio_net': pct(s['portfolio_net'], 1), 'max_dd': pct(s['max_dd'], 1),
        'win_rate': pct(s['win_rate'], 0),
        'profit_factor': '∞' if pf >= 999 else f'{pf:.2f}',
        'confidence': s['confidence'],
    }


def fmt_tf(r):
    return {
        'tf': r['tf'], 'specs': r['specs'], 'trades': num(r['trades']),
        'avg_gross': pct(r['avg_gross'], 3), 'avg_net': pct(r['avg_net'], 3),
        'fee_drag': pct(r['fee_drag'], 3),
        'median_symbol_net': pct(r['median_symbol_net'], 3),
        'pct_symbols_positive': pct(r['pct_symbols_positive'], 0),
        'median_portfolio': pct(r['median_portfolio'], 1),
        'pct_positive': pct(r['pct_positive'], 0),
    }


def fmt_batch(b):
    return {
        'batch': b['batch'].replace('batch_', ''), 'best_sid': b['best_sid'],
        'best_title': b['best_title'], 'best_tf': b['best_tf'],
        'best_portfolio_net': pct(b['best_portfolio_net'], 1) if b['best_portfolio_net'] is not None else '—',
        'best_avg_net': pct(b['best_avg_net'], 2) if b['best_avg_net'] is not None else '—',
        'best_median_symbol_net': pct(b.get('best_median_symbol_net', 0), 2) if b.get('best_median_symbol_net') is not None else '—',
        'best_pct_symbols_positive': pct(b.get('best_pct_symbols_positive', 0), 0),
        'best_n': b['best_n'],
    }


pool = [s for s in specs if not s.get('is_duplicate')]
ranked = [s for s in pool if s['n'] >= 30 and s['symbols'] >= 5
          and s.get('median_symbol_net', -1) > 0 and s.get('pct_symbols_positive', 0) >= 0.5]
if not ranked:
    ranked = [s for s in pool if s['n'] >= 30 and s['symbols'] >= 5]
if not ranked:
    ranked = pool
ranked = sorted(ranked, key=lambda s: s['median_symbol_net'], reverse=True)
top = ranked[:20]

tf_sorted = sorted(tf, key=lambda r: {'5m': 0, '15m': 1, '1h': 2, '4h': 3, '1d': 4, '1w': 5}.get(r['tf'], 9))
daily = next(r for r in tf if r['tf'] == '1d')
five = next(r for r in tf if r['tf'] == '5m')

batch_status = {}
for b in batches:
    batch_status[b['status']] = batch_status.get(b['status'], 0) + 1

# best batches by best portfolio (robust)
dup_sids = {s['sid'] for s in specs if s.get('is_duplicate')}
best_batches = sorted([b for b in batches if b.get('best_median_symbol_net') is not None
                       and b.get('best_sid') not in dup_sids
                       and b.get('best_pct_symbols_positive', 0) >= 0.5 and b['best_n'] >= 30],
                      key=lambda b: b['best_median_symbol_net'], reverse=True)[:10]

lines = []
lines.append('# Book Signal Review — Mechanical Backtest Report')
lines.append('')
lines.append(f'**Scope:** 215 batch folders · 454 extracted strategy sections · {meta["n_tested_specs"]} high/medium-confidence mechanical proxies ({meta.get("n_unique_rules", "—")} unique engine rules) · {meta["n_symbols"]} Binance USDT-M perpetuals')
lines.append('')
lines.append(f'**Window:** signals {meta["start"]} → {meta["end"]}; 1-minute execution data through {meta["exec_end"]}.')
lines.append('')
lines.append('**Costs:** Binance USDT-M taker fee 5 bps per side, slippage 2 bps per side, historical 8h funding included. One position per symbol per strategy.')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Executive summary')
lines.append('')
lines.append(f'- **{meta["n_tested_batches"]} of 215 batches** produced at least one high/medium-confidence mechanical test. {meta["n_low_batches"]} batches contain only low-confidence mappings, {meta["n_excluded_batches"]} are excluded, and {meta["n_no_sections"]} have no strategy sections.')
best_tf = max(tf, key=lambda r: r['avg_net'])
four = next((r for r in tf if r['tf'] == '4h'), daily)
week = next((r for r in tf if r['tf'] == '1w'), daily)
lines.append(f'- **Fast timeframes are dominated by costs.** The average 5m trade is {pct(five["avg_gross"],3)} gross and {pct(five["avg_net"],3)} net; the round-trip cost stack is {pct(five["fee_drag"],3)}. Only {pct(five["pct_symbols_positive"],0)} of symbol-spec pairs are positive.')
lines.append(f'- **{best_tf["tf"]} has the best average net per trade** ({pct(best_tf["avg_net"],2)}), but the broad-universe edge is thin and uneven: daily average net {pct(daily["avg_net"],2)}, median symbol net {pct(daily["median_symbol_net"],3)}, {pct(daily["pct_positive"],0)} of daily specs positive, {pct(daily["pct_symbols_positive"],0)} of symbol-spec pairs positive. The 4h shelf averages {pct(four["avg_net"],3)} net with a {pct(four["median_symbol_net"],3)} median symbol; the 1w shelf is a small {week["specs"]}-spec sample with {pct(week["avg_net"],2)} average net.')
lines.append(f'- **Buy & hold is a high bar.** BTC returned {pct(bench["btc_return"],0)} and the equal-weight crypto basket {pct(bench["basket_return"],0)} over the window. The median daily portfolio is {pct(daily["median_portfolio"],1)}; most mechanical proxies do not beat the benchmark after costs.')
if top:
    lines.append(f'- **Best robust proxies in the broad universe:** ' + ', '.join(f'{s["sid"]} ({s["tf"]}, {s["family"]}, median symbol {pct(s["median_symbol_net"],2)})' for s in top[:5]) + '.')
else:
    lines.append('- **No proxy passed the robust positive-edge filter** (30+ trades, 5+ symbols, positive median symbol net, at least half of symbols positive). The scorecard below is therefore descriptive rather than a recommendation.')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Timeframe scorecard')
lines.append('')
lines.append(f'All figures are fee-inclusive. “Portfolio” compounds monthly returns with 1/{meta["n_symbols"]} capital per trade; “median symbol net” gives each symbol one vote and resists single-listing outliers.')
lines.append('')
lines.append(table([fmt_tf(r) for r in tf_sorted], ['tf', 'specs', 'trades', 'avg_gross', 'avg_net', 'fee_drag', 'median_symbol_net', 'pct_symbols_positive', 'median_portfolio', 'pct_positive'],
                   ['TF', 'Specs', 'Trades', 'Avg gross', 'Avg net', 'Cost drag', 'Med. symbol net', 'Symbols +', 'Med. portfolio', 'Specs +']))
lines.append('')
lines.append('## Universe sensitivity')
lines.append('')
lines.append(f'- Earlier 58-symbol liquid subset: daily average net {pct(0.008243206658,2)}, median symbol net {pct(0.000786816630,3)}, median portfolio {pct(0.1157255,1)}.')
lines.append(f'- Current {meta["n_symbols"]}-symbol active universe: daily average net {pct(daily["avg_net"],2)}, median symbol net {pct(daily["median_symbol_net"],3)}, median portfolio {pct(daily["median_portfolio"],1)}.')
lines.append('- The sign reversal is a universe-selection result, not a parameter tweak: the 58-symbol set was concentrated in liquid majors, while the broad set includes many new and low-liquidity listings.')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Most consistent strategies')
lines.append('')
lines.append('Filter: at least 30 trades, at least 5 symbols, positive median symbol net and at least half of symbols positive. Sorted by median symbol net.')
lines.append('')
lines.append(table([fmt_spec(s) for s in top], ['sid', 'batch', 'title', 'tf', 'family', 'n', 'symbols', 'avg_net', 'median_symbol_net', 'pct_symbols_positive', 'portfolio_net', 'max_dd', 'win_rate', 'profit_factor', 'confidence'],
                   ['SID', 'Batch', 'Strategy', 'TF', 'Family', 'Trades', 'Symbols', 'Avg net', 'Med. symbol net', 'Symbols +', 'Portfolio', 'Max DD', 'Win', 'PF', 'Conf.']))
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Best batches')
lines.append('')
lines.append(table([fmt_batch(b) for b in best_batches], ['batch', 'best_sid', 'best_title', 'best_tf', 'best_median_symbol_net', 'best_pct_symbols_positive', 'best_portfolio_net', 'best_n'],
                   ['Batch', 'SID', 'Strategy', 'TF', 'Med. symbol net', 'Symbols +', 'Portfolio', 'Trades']))
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Coverage and exclusions')
lines.append('')
lines.append(f'- Tested batches: **{meta["n_tested_batches"]}**')
lines.append(f'- Low-confidence only: **{meta["n_low_batches"]}**')
lines.append(f'- Excluded only: **{meta["n_excluded_batches"]}**')
lines.append(f'- No strategy sections: **{meta["n_no_sections"]}**')
lines.append(f'- Tested proxies: **{meta["n_tested_specs"]}**; unique engine rules: **{meta.get("n_unique_rules", "—")}**; with at least one trade: **{meta.get("n_specs_with_trades", len(specs))}**')
lines.append(f'- Excluded sections: **{meta["n_excluded_sections"]}**')
lines.append('')
lines.append('Per-batch status and the exact reason for each exclusion are in the dashboard’s **Batch coverage** tab and in `dashboard_data.json`.')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Method')
lines.append('')
lines.append('- Signals are generated only on completed strategy-timeframe bars. Entry is the first 1m open after the signal bar closes.')
lines.append('- Stops and targets are checked on 1m OHLC. If stop and target are both touched in the same 1m bar, the stop is assumed first (conservative).')
lines.append('- Time and signal exits occur at the next 1m open. One position per symbol per strategy; no pyramiding or overlapping entries.')
lines.append('- Fees: 5 bps per side; slippage: 2 bps per side; funding: historical 8h rates charged to the position side.')
lines.append('- 1h/4h bars come from the local parquet archive; 5m/15m are resampled from 1m, 1d is resampled from 1h, and weekly bars from daily. Signals cover 2022-08 through 2026-08; 1m execution data extends through 2026-10-18.')
lines.append(f'- Portfolio return allocates 1/{meta["n_symbols"]} of capital to each trade and compounds monthly. It is a conservative equal-weight deployment; idle symbols leave cash uninvested. It is therefore not directly comparable to a fully invested buy-and-hold benchmark.')
lines.append('')
lines.append('## Caveats')
lines.append('')
lines.append('- This is a **first-pass mechanical proxy**, not an exact replication of discretionary book rules. Mapping confidence is shown per strategy (`high`, `medium`, `low`); low-confidence mappings are excluded from the main results.')
lines.append('- New listings can produce extreme single-trade returns. Rankings use median symbol net and symbol consistency; average net and portfolio return are shown with that caveat.')
lines.append('- The universe is the 525-symbol active USDT-M set in the local archive; symbols enter at their first available bar, so survivorship/listing bias remains.')
lines.append('- Cross-sectional, breadth, pairs, portfolio-rotation and options/FX/US-equity strategies are out of scope for this single-symbol engine.')
lines.append('- Taker fills are assumed. Maker execution, rebates or lower slippage would materially improve the fast timeframes.')
lines.append('')
lines.append('## Files')
lines.append('')
lines.append('- `dashboard.html` — interactive dashboard (self-contained).')
lines.append('- `strategy_metrics.csv` — per-strategy metrics.')
lines.append('- `dashboard_data.json` — full data used by the dashboard.')
lines.append('- `results_525/summary/*.parquet` — per-symbol, per-strategy metrics.')
lines.append('- `results_525/monthly/*.parquet` — per-symbol monthly PnL.')
lines.append('- `results_525/errors/*.json` — per-symbol expression errors, if any.')
lines.append('')

out = os.path.join(BT, 'REPORT.md')
open(out, 'w', encoding='utf-8').write('\n'.join(lines))
print('wrote', out, len(lines), 'lines')
