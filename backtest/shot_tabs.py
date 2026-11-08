from playwright.sync_api import sync_playwright

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
url = 'file:///D:/Paper_ML_BSH/analysis/book_signal_review/backtest/dashboard.html'
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', headless=True)
    page = b.new_page(viewport={'width': 1600, 'height': 2400}, device_scale_factor=1)
    page.goto(url)
    page.wait_for_timeout(1500)
    page.click('button[data-tab="batches"]')
    page.wait_for_timeout(500)
    print('batch rows:', page.eval_on_selector_all('#batchTable tbody tr', 'els => els.length'))
    print('batch statuses:', page.eval_on_selector_all('#batchTable tbody tr', 'els => els.slice(0,3).map(e=>e.innerText.split("\\n").slice(0,3).join(" | "))'))
    page.screenshot(path=BT + r'\tab_batches.png', full_page=True)
    page.click('button[data-tab="method"]')
    page.wait_for_timeout(500)
    page.screenshot(path=BT + r'\tab_method.png', full_page=True)
    b.close()
print('done')
