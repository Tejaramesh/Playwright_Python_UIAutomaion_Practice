from playwright.sync_api import sync_playwright,expect

def test_radiobutton():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://testing.qaautomationlabs.com/radio-button.php")
        #Locate Radio buttons
        maleradio=page.locator("input[value='Male'][name='gender']")
        femaleradio=page.locator("input[value='Female'][name='gender']")
        #Assert radio buttons are visible and enabled
        expect(maleradio).to_be_visible()
        expect(maleradio).to_be_enabled()
        expect(femaleradio).to_be_visible()
        expect(femaleradio).to_be_enabled()
        maleradio.wait_for(state="visible",timeout=40000)
        maleradio.check()
        expect(maleradio).to_be_checked()
        expect(femaleradio).not_to_be_checked()
        #Print status of radio button
        print("Male radio selected:", maleradio.is_checked())
        print("Female radio selected:", femaleradio.is_checked())
        page.get_by_role("button",name="Show Selected Gender").click()
        page.wait_for_selector("[data-testid='radio-result']")
        result=page.locator("[data-testid='radio-result']")
        expect(result).to_contain_text("You selected: Male")
        #select female radio button and assert
        femaleradio.check()
        expect(femaleradio).to_be_checked()
        expect(maleradio).not_to_be_checked()
        page.get_by_role("button",name="Show Selected Gender").click()
        page.wait_for_selector("[data-testid='radio-result']")
        result=page.locator("[data-testid='radio-result']")
        expect(result).to_contain_text("You selected: Female")
        page.pause()


