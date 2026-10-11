import pytest
from playwright.sync_api import expect, sync_playwright
Expected_url_after_login="https://ecommerce-playground.lambdatest.io/index.php?route=account/account"

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
        page.get_by_label("E-Mail Address").fill("timcook@yopmail.com")
        page.get_by_label("Password").fill("Test@1234")
        page.get_by_role("button",name="Login").click()
        expect(page).to_have_url(Expected_url_after_login)
        expect(page).to_have_title("My Account")
        expect(page.get_by_role("heading",name="My Account")).to_be_visible()
