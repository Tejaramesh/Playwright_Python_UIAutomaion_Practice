from playwright.sync_api import sync_playwright,expect
import pytest
import sys

@pytest.mark.skip(reason="Feature is under development")
def test_homepage_loads_testCase():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://qaautomationlabs.com")
        assert page.title()=='Home - QA Automation Labs'

@pytest.mark.xfail(reason="Known bug in checkout page")
def test_anntation_fail_testCase():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://qaautomationlabs.com/")
        assert page.title() =="Home - QA Automation Labs1"

@pytest.mark.skipif(sys.platform == "win32", reason="does not run on Windows")
def test_annotation_skipIf_testcase():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://naveenautomationlabs.com/opencart/index.php?rout=account/login")
        expect(page,"The page title did not match the expected value. ").to_have_title("Account Login")
        expect(page.locator("#input-email")).to_have_attribute("type","text")

@pytest.mark.skip_browser("firefox",reason="Firefox doesn't support this feature")
def test_annotation_skip_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/login")
        expect(page,"The page title did not match the expected value.")
