from playwright.sync_api import sync_playwright,expect

def test_draganddrop():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://testing.qaautomationlabs.com/drag-and-drop.php")
        page.wait_for_load_state("load")
        page.wait_for_timeout(5000)
        # source_element="ul#sortableList>li:has-text('Item 1')"
        # target_element="ul#sortableList>li:has-text('Item 5')"
        # source_element=page.get_by_title("Drag Item 3: Personal")
        # target_element=page.get_by_title("Drag Item 1: Inbox")
        page.drag_and_drop("ul#sortableList>li:has-text('Item 1')","ul#sortableList>li:has-text('Item 5')")
        #source_element.drag_to(target_element)
        page.wait_for_timeout(5000)
        page.pause()

