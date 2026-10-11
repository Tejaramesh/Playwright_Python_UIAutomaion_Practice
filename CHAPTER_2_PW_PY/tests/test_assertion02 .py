from playwright.sync_api import sync_playwright,expect
import pytest

@pytest.mark.smoke
def test_successful_login_no_error():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/shop.php")
        page.get_by_placeholder("Email").fill("wrong@demo.com")
        page.get_by_placeholder("Password").fill("Wrongpass")
        page.get_by_role("button", name="Login").click()
        expect(page.get_by_text("Invalid email or password!")).to_be_visible()

@pytest.mark.sanity
def test_endtoendassertion():
    with sync_playwright() as p:
        browser=p.chromium.launch()
        page=browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.get_by_title("Email").fill("demo@demo.com")
        page.fill("input[title='Password']","demo")
        page.get_by_role("button",name="Login").click()
        # verify initial cart is empty
        expect(page.locator("#cartcount")).to_have_count(0)
        page.get_by_title("Shop Men Fashion").click()
        page.get_by_role("link",name="Black T-Shirt").click()
        page.get_by_title("Add Black T-Shirt to cart").click()
        expect(page.locator("#cartCount")).to_have_text("1")
        page.locator("[title='Cart']").click()
        print(page.locator("#cartTable>tbody").inner_text())
        assert page.locator("#cartTable>tbody").inner_text().count("Black T-Shirt")>0 
        expect(page.locator("#cartTable>tbody")).to_contain_text("Black T-Shirt")  

@pytest.mark.regression
def test_handlingjs():
    with sync_playwright() as p:
        browser=p.chromium.launch()
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
