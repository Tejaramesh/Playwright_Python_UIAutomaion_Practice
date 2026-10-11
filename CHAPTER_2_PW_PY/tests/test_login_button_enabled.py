from playwright.sync_api import sync_playwright,expect,Page

# def test_loginbutton():
#     with sync_playwright() as p:
#         browser=p.chromium.launch(headless=False)
#         page=browser.new_page()
#         page.goto("https://shop.qaautomationlabs.com/shop.php")
#         ele=page.get_by_role("button",name="Login")
#         expect(ele).not_to_be_disabled()

def test_success_login_no_error():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/login")
        page.get_by_role('textbox',  name= 'E-Mail Address').fill("johnpeter123@yopmail.com")
        page.get_by_label('Password').fill("Test@ 1234")
        page.get_by_role('button',name='Login').click()
        page.pause()
        expect(page.locator("body")).not_to_contain_text("Warning: No match for E-Mail Address")

