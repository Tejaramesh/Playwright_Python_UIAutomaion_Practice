from playwright.sync_api import sync_playwright

def test_handletabs():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page1=context.new_page()
        page1.goto("https://qaautomationlabs.com")
        print(f"Tab 1 Title:{page1.title()}")
        #create second tab and navigate to another website
        page2=context.new_page()
        page2.goto("https://www.python.org")
        print(f"Tab 2 Title: {page2.title()}")
        #simulate clicking a link that opens a new tab
        #using a demp site that opens a new tab on click
        page1.goto("https://the-internet.herokuapp.com/windows",timeout=60000)
        page1.wait_for_load_state("domcontentloaded",timeout=60000)
        with context.expect_page() as new_page:
            page1.get_by_role('link', name='Click Here').click(timeout=60000)
        page3=new_page.value
        print(f"Tab 3 Title: {page3.title()}")
        #bring back to front
        page1.bring_to_front()
        print(f"switched back to Tab1: {page1.title()}")
        #Interact with second tab
        page2.bring_to_front()
        page2.get_by_role('searchbox',  name= 'Search This Site').fill("playwright python")
        page2.get_by_role("button",name="Go").click()
        print(f"performed search in Tab 2: {page2.title()}")
        #List all open tabs
        print("\nAll open tabs:")
        for i, page in enumerate(context.pages):
            print(f"Tab {i+1} {page.title()}")

        page3.close()
        print("\nClosed Tab3")
        #verify remaining tabs
        print("\nRemaining tabs:")
        for i ,page in enumerate(context.pages):
            print(f"Tab {i+1} : {page.title()}")
        browser.close()


