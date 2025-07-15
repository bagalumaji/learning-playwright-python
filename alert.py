from playwright.sync_api import sync_playwright

def test_alert_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://testautomationpractice.blogspot.com/")

        #need to update --> now its not working
        with page.expect_dialog() as dialog_info:
            page.click("#alertBtn")

        dialog = dialog_info.value
        print("Alert message:", dialog.message)
        dialog.accept()

        browser.close()
