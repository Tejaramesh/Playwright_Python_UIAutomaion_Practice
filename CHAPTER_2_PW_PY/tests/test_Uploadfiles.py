from playwright.sync_api import sync_playwright,expect

def test_uploadfile():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://testing.qaautomationlabs.com/file-upload.php")
        file_path="C:\\Users\\admin\\playwright-python-project\\CHAPTER_2_PW_PY\\testfiles\\Teja R_Resume.pdf"
        field=page.get_by_title("Browse for a file to upload")
        page.set_input_files("[title='Browse for a file to upload']",file_path)
        page.wait_for_timeout(5000)
        file_info=page.locator("#fileInfo").inner_text()
        print("Uploaded file info",file_info)
        browser.close()

