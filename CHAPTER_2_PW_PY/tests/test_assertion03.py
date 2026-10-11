from playwright.sync_api import sync_playwright,expect

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