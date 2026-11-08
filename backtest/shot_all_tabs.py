from playwright.sync_api import sync_playwright
import os, sys

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
url = 'file:///D:/Paper_ML_BSH/analysis/book_signal_review/backtest/dashboard.html'
errors = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', headless=True)
    page = b.new_page(viewport={'width': 1600, 'height': 2200}, device_scale_factor=1)
    page.on('pageerror', lambda e: errors.append(f'pageerror: {e}'))
    page.on('console', lambda m: errors.append(f'console {m.type}: {m.text}') if m.type == 'error' else None)
    page.goto(url)
    page.wait_for_timeout(1800)
    print('title:', page.title())
    print('KPI:', page.eval_on_selector_all('.kpi .v', 'els=>els.map(e=>e.textContent)'))
    print('KPI sub:', page.eval_on_selector_all('.kpi .s', 'els=>els.map(e=>e.textContent)'))
    print('findings:', page.eval_on_selector_all('.finding h3', 'els=>els.map(e=>e.textContent)'))
    page.screenshot(path=os.path.join(BT, 'final_overview.png'), full_page=True)

    page.click('button[data-tab="strategies"]')
    page.wait_for_timeout(700)
    print('strategy rows:', page.eval_on_selector_all('#specTable tbody tr', 'els=>els.length'))
    print('count label:', page.inner_text('#count'))
    page.screenshot(path=os.path.join(BT, 'final_strategies.png'), full_page=False)

    page.click('button[data-tab="batches"]')
    page.wait_for_timeout(500)
    print('batch rows:', page.eval_on_selector_all('#batchTable tbody tr', 'els=>els.length'))
    page.screenshot(path=os.path.join(BT, 'final_batches.png'), full_page=False)

    page.click('button[data-tab="method"]')
    page.wait_for_timeout(500)
    page.screenshot(path=os.path.join(BT, 'final_method.png'), full_page=True)
    print('errors:', errors[:10])
    b.close()
print('done')
