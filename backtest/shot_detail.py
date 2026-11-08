from playwright.sync_api import sync_playwright

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
url = 'file:///D:/Paper_ML_BSH/analysis/book_signal_review/backtest/dashboard.html'
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', headless=True)
    page = b.new_page(viewport={'width': 1600, 'height': 1600}, device_scale_factor=1)
    page.on('pageerror', lambda e: errs.append(str(e)))
    page.on('console', lambda m: errs.append('console:' + m.text) if m.type == 'error' else None)
    page.goto(url)
    page.wait_for_timeout(1200)
    page.click('button[data-tab="strategies"]')
    page.wait_for_timeout(300)
    page.click('#specTable tbody tr:first-child')
    page.wait_for_timeout(500)
    print('detail on:', page.eval_on_selector('#detail', 'e => e.classList.contains("on")'))
    print('detail title:', page.eval_on_selector('#dTitle', 'e => e.textContent'))
    print('detail metrics:', page.eval_on_selector('#dMets', 'e => e.innerText.replace(/\\n/g," | ")')[:300])
    print('detail chart nodes:', page.eval_on_selector_all('#dChart svg', 'els => els.length'))
    print('errors:', errs[:5])
    b.close()
print('done')
