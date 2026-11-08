import os, glob, json
import pandas as pd

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
summ = glob.glob(os.path.join(BT, 'results_525', 'summary', '*.parquet'))
mon = glob.glob(os.path.join(BT, 'results_525', 'monthly', '*.parquet'))
print('summary_files', len(summ), 'monthly_files', len(mon))

d = json.load(open(os.path.join(BT, 'dashboard_data.json'), encoding='utf-8'))
print('meta', {k: d['meta'].get(k) for k in ['n_symbols','n_tested_specs','n_unique_rules','n_specs_with_trades','n_summary_rows','n_monthly_rows']})
print('tf')
for r in d['tf']:
    print(r['tf'], r['specs'], r['trades'], round(r['avg_net']*100,4), round(r['median_symbol_net']*100,4), round(r['pct_symbols_positive']*100,2), round(r['median_portfolio']*100,2))
pool = [s for s in d['specs'] if not s.get('is_duplicate')]
top = sorted(pool, key=lambda s: s.get('median_symbol_net', -1), reverse=True)[:15]
print('top unique')
for s in top:
    print(s['sid'], s['tf'], round(s['median_symbol_net']*100,3), round(s['pct_symbols_positive']*100,1), s['n'], s['symbols'])
print('dup groups >1', sum(1 for s in d['specs'] if s.get('rule_group_size',1)>1))
print('missing fields', [s['sid'] for s in d['specs'] if not s.get('rule_key')][:5])
print('benchmark', d['benchmark']['btc_return'], d['benchmark']['basket_return'])
