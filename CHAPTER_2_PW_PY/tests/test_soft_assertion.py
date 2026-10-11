from playwright.sync_api import sync_playwright
import pytest
def test_soft_assertions():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://naveenautomationlabs.com/opencart/index.php?route=common/home")
       # expectequal(page.title(),"Your Store","Page title mismatch")
        logo=page.get_by_alt_text("naveenopencart")
        #assert.is_true(logo.is_visible(),"Logo should be visible on homepage")
