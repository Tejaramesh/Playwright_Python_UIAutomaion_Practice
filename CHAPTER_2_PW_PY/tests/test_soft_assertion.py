from playwright.sync_api import sync_playwright,Page,expect
import pytest_check as check

def test_soft_assertions(page:Page):
    # with sync_playwright() as p:
    #     browser=p.chromium.launch(headless=False)
    #     page=browser.new_page()
        page.goto("https://naveenautomationlabs.com/opencart/index.php?route=common/home")
        check.equal(page.title(),"Your Store","Page title mismatch")
        logo=page.get_by_alt_text("naveenopencart")
        check.is_true(logo.is_visible(),"Logo should be visible on homepage")
