from playwright.sync_api import expect, sync_playwright

def test_endtoend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/login")
        page.get_by_label("E-Mail Address").fill("johnpeter123@yopmail.com")
        page.get_by_label("Password").fill("Test@1234")
        page.locator("[value='Login']").click()
        expect(page.locator("h2:has-text('My Account')")).to_be_visible()
        expect(page.locator("h2:has-text('My Orders')")).to_be_visible()
        expect(page.locator("h2:has-text('My Affiliate Account')")).to_be_visible()
        expect(page.locator("h2:has-text('Newsletter')")).to_be_visible()
        page.get_by_alt_text("naveenopencart").click()
        page.locator(".product-thumb").filter(has_text="MacBook").click()
        page.get_by_role('button').filter(has_text="Add to Cart").first.click()
        expect(page.locator(".alert-success")).to_contain_text("Success: You have added MacBook to your shopping cart!")
        page.locator("#cart-total").click()
        page.locator("a>strong").filter(has_text="Checkout").click()
        page.locator("[title='My Account']").click()
        page.get_by_text("Logout").click()
