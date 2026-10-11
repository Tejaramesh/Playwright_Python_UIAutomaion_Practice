from playwright.sync_api import sync_playwright,expect
def test_iframe():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://www.lambdatest.com/selenium-playground/iframe-demo/")
        #frame=page.frame(url="https://www.testmuai.com/selenium-playground/iframe-demo/contant/")
        # frame=page.frame_locator("#iFrame1")
        page.frame_locator().locator(".rsw-ce").fill("Hi I am Teja")
        #frame2=page.frame(url="https://consentcdn.cookiebot.com/sdk/bc-v4.min.html")
        page.locator("iframe").nth(1).content_frame.get_by_role("link", name="Start free with Google").is_visible()
        page.pause()