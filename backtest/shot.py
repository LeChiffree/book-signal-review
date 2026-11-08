from playwright.sync_api import sync_playwright

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
url = 'file:///D:/Paper_ML_BSH/analysis/book_signal_review/backtest/dashboard_preview_strategies_v6.html'
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', headless=True)
    page = b.new_page(viewport={'width': 1600, 'height': 2400}, device_scale_factor=1)
    page.goto(url)
    page.wait_for_timeout(1500)
    print('count:', page.eval_on_selector('#count', 'e => e.textContent'))
    print('rows:', page.eval_on_selector_all('#specTable tbody tr', 'els => els.length'))
    print('rt rows:', page.eval_on_selector_all('#specTable tbody tr', "els => els.filter(e => e.textContent.includes('RT152C')).length"))
    print('uniq checked:', page.eval_on_selector('#uniqOnly', 'e => e.checked'))
    page.screenshot(path=BT + r'\preview_strategies_pw.png', full_page=True)
    b.close()
print('done')
