import sys, re
BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
tab = sys.argv[1] if len(sys.argv) > 1 else 'strategies'
h = open(BT + r'\dashboard.html', encoding='utf-8').read()
# deactivate all tabs/panels
h = h.replace('class="tab active"', 'class="tab"')
h = h.replace('class="panel active"', 'class="panel"')
# activate requested
h = h.replace(f'class="tab" data-tab="{tab}"', f'class="tab active" data-tab="{tab}"')
h = h.replace(f'class="panel" id="panel-{tab}"', f'class="panel active" id="panel-{tab}"')
# make the browser show that tab on load
h = h.replace('initOverview();renderSpecs();renderBatches();', f'initOverview();renderSpecs();renderBatches();showTab("{tab}");')
open(BT + rf'\dashboard_preview_{tab}.html', 'w', encoding='utf-8').write(h)
print('wrote', len(h))
