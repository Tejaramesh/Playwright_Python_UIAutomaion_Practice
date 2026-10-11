from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://qaautomationlabs.com/")
    print(page.title())
    page.screenshot(path="playwright.png")
    browser.close()