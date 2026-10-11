from playwright.sync_api import sync_playwright,expect
import os

def test_downloadfile():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://testing.qaautomationlabs.com/file-download.php")
        page.wait_for_load_state("load")
        page.locator("#textInput").fill("Testing file download successfully")
        page.get_by_role("button",name="Generate File").click()
        with page.expect_download() as download_info:
            page.get_by_role("link",name="Download File").click()
            download=download_info.value

        #step 3: Save the downloaded file under downloads folder
        os.makedirs("downloads",exist_ok=True)
        download.save_as(os.path.join("downloads","playwright_test_file.txt"))
            
        page.get_by_role("link",name="Download File").click()
        page.pause()