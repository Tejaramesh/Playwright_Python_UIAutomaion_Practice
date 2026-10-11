from playwright.sync_api import sync_playwright,expect

def test_handlingjs():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://testing.qaautomationlabs.com/javaScript-alert.php")
        page.locator("[title='Show JavaScript alert']").click()
        #page.pause()
        page.on("dialog",lambda dialog:dialog.accept())
        page.get_by_title("Show JavaScript confirm").click()
        page.on("dialog",lambda dialog:dialog.dismiss())
        #page.pause()
        page.get_by_title("Show JavaScript prompt").click()
        page.on('dialog',lambda dialog:dialog.type("test"))
        page.on('dialog',lambda dialog:print(dialog.message()))
        
        