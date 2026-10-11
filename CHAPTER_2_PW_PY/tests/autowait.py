from playwright.sync_api import Page,expect

def test_autowait(page:Page):
    page.goto("https://www.amazon.in/")
    page.locator("#twotabsearchtextbox[placeholder='Search Amazon.in']").fill("Playwright Book")
    page.locator("[type='submit']").click()
    page.wait_for_selector("[data-component-type='s-search-results']",timeout=10000)
    print("Closing the browser....")
    page.close()