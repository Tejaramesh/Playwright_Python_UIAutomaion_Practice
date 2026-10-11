from playwright.sync_api import sync_playwright,expect

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.amazon.in")
    #Enter search query and submit
    page.fill("#twotabsearchtextbox","Laptop")
    page.click("#nav-search-submit-text [type='submit']")

    #wait for search results URL to load
    page.wait_for_url("**/s?k=Laptop*")
    print("Navigated to search results for laptop")
    browser.close()