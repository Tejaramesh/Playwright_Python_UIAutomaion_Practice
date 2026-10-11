from playwright.sync_api import sync_playwright,expect

def test_shadowdom():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://www.testmuai.com/selenium-playground/shadow-dom/")
        page.wait_for_load_state("networkidle")
        page.locator("[name='username']").fill("play_user")
        page.locator("[name='email'][classname='form-control']").fill("play_user@test.com")
        page.locator("[name='password']").fill("P@ssw0rd!")
        page.locator("[name='confirm_password']").fill("P@ssw0rd!")
        page.get_by_role("button",name="Submit").click()
        page.pause()