import json

p = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\dashboard_data.json'
d = json.load(open(p, encoding='utf-8'))
ss = [s for s in d['specs'] if not s.get('is_duplicate') and s['n'] >= 30 and s['symbols'] >= 5]
ss.sort(key=lambda s: s['median_symbol_net'], reverse=True)
for i, s in enumerate(ss[:25], 1):
    print('%2d %-8s %-3s %-15s medsym=%6.2f%% sym+=%3.0f%% pf=%7.1f%% n=%4d syms=%2d %s' % (
        i, s['sid'], s['tf'], s['family'], s['median_symbol_net'] * 100,
        s['pct_symbols_positive'] * 100, s['portfolio_net'] * 100, s['n'], s['symbols'],
        s['title'][:60]))
