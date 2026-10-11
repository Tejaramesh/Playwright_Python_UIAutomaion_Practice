from playwright.sync_api import sync_playwright,expect
from pytest_check import check

def test_inputfield():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/")
        email=page.get_by_title("Email")
        #Assertions for email input field
        expect(email).to_be_visible()
        expect(email).to_be_enabled()
        expect(email).to_be_editable()
        expect(email).to_be_empty()
        password=page.get_by_placeholder("Password")
        #Assertions for password input field
        with check("Password should be visible"):
            expect(password).to_be_visible(timeout=40000)

        with check("Password should be enabled"):
            expect(password).to_be_enabled()
        expect(password).to_be_editable()
        expect(password).to_be_empty()
        email.fill("demo@demo.com")
        print("cam here till last")
        password.fill("demo")
        loginbtn=page.get_by_role("button").filter(has_text="Login")
        expect(loginbtn).to_be_visible()    
        expect(loginbtn).to_be_enabled()
        loginbtn.click()
        page.get_by_role("link",name="Shop Men Fashion").click()
        formal=page.locator("label[for='gender-1']")
        footwear=page.locator("label[for='gender-2']")
        formal.wait_for(state="visible",timeout=40000)
        formal.is_enabled()
        expect(formal).to_be_visible()
        expect(footwear).to_be_visible()
        formal.click()
        footwear.click()
        print("Formal checkbox checked: ",formal.is_checked())
        print("Footwear checkbox checked: ",footwear.is_checked())
        page.wait_for_timeout(5000)
        formal.uncheck()
        footwear.uncheck()
        expect(formal).not_to_be_checked()
        expect(footwear).not_to_be_checked()
        print("Formal checkbox checked: ",formal.is_checked())
        print("Footwear checkbox checked: ",footwear.is_checked())

        