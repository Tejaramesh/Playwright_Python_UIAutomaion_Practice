from pathlib import Path

from playwright.sync_api import sync_playwright

def test_uploadfile():
    with sync_playwright() as p:
        browser=p.chromium.launch()
        page=browser.new_page()
        page.goto("https://testing.qaautomationlabs.com/file-upload.php")
        file_path = Path(__file__).resolve().parents[1] / "testfiles" / "Teja R_Resume.pdf"
        field=page.get_by_title("Browse for a file to upload")
        field.set_input_files(str(file_path))
        page.wait_for_timeout(5000)
        file_info=page.locator("#fileInfo").inner_text()
        print("Uploaded file info",file_info)
        browser.close()
