import re
p = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\dashboard_preview_strategies.html'
h = open(p, encoding='utf-8').read()
for m in re.finditer(r'renderSpecs\(\)', h):
    print(m.start(), repr(h[m.start()-80:m.start()+80]))
print('--- init calls ---')
for m in re.finditer(r'initOverview\(\)', h):
    print(m.start(), repr(h[m.start()-80:m.start()+120]))
