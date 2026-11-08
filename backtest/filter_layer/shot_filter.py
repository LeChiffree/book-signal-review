from playwright.sync_api import sync_playwright
import os

ROOT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\filter_layer'
url = 'file:///D:/Paper_ML_BSH/analysis/book_signal_review/backtest/filter_layer/filter_dashboard.html'
errors = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', headless=True)
    page = b.new_page(viewport={'width': 1600, 'height': 2200}, device_scale_factor=1)
    page.on('pageerror', lambda e: errors.append(f'pageerror: {e}'))
    page.on('console', lambda m: errors.append(f'console {m.type}: {m.text}') if m.type == 'error' else None)
    page.goto(url + '?v=final')
    page.wait_for_timeout(1800)
    print('title:', page.inner_text('#title'))
    print('kpis:', page.inner_text('#kpis').replace('\n', ' | '))
    print('rows:', page.eval_on_selector_all('#resultTable tbody tr', 'els=>els.length'))
    page.screenshot(path=os.path.join(ROOT, 'filter_overview.png'), full_page=True)

    # pick a filter with a decent number of results
    btns = page.query_selector_all('#filterList button')
    if len(btns) > 2:
        btns[2].click()
        page.wait_for_timeout(600)
        page.screenshot(path=os.path.join(ROOT, 'filter_selected.png'), full_page=False)
    print('errors:', errors[:6])
    b.close()
print('done')
