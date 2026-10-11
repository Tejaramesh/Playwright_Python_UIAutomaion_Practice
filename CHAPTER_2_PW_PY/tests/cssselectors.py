from playwright.sync_api import sync_playwright

def test_CSS_ID_Selector():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://qaautomationlabs.com/testing/form.php")
        page.get_by_test_id("form-firstname").fill("John")
        page.pause()


def test_xpath_selector():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://qaautomationlabs.com/testing/web-table.php")
        page.wait_for_selector("#dataTable>tbody>tr:nth-child(4)>td:nth-child(2)")
        cell=page.locator("#dataTable>tbody>tr:nth-child(4)>td:nth-child(2)")
        text=cell.inner_text()
        print(f"Cell Content Is ==>: {text}")
        page.pause()


def test_textBased_selector():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page();
        page.goto("https://qaautomationlabs.com/testing/radio-button.php")
        page.get_by_label("Radio Button 2").check()
        page.wait_for_timeout(2000)
        print("Hi !! Radio Button 2 is selected")
        page.pause()
        browser.close()
