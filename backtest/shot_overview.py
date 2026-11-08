from playwright.sync_api import sync_playwright

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
url = 'file:///D:/Paper_ML_BSH/analysis/book_signal_review/backtest/dashboard.html'
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', headless=True)
    page = b.new_page(viewport={'width': 1600, 'height': 2400}, device_scale_factor=1)
    page.goto(url)
    page.wait_for_timeout(2000)
    print('KPI sub:', page.eval_on_selector_all('.kpi .s', 'els => els.map(e => e.textContent)'))
    print('findings:', page.eval_on_selector_all('.finding', 'els => els.map(e => e.innerText.replace(/\\n/g, " | "))'))
    print('tf rows:', page.eval_on_selector_all('#tfTable tbody tr', 'els => els.length'))
    page.screenshot(path=BT + r'\overview_pw.png', full_page=True)
    b.close()
print('done')
