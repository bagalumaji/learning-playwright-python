from playwright.sync_api import Page


def test_file_upload_demo(page:Page):
    page.goto("http://testautomationpractice.blogspot.com/")
    page.locator("id=singleFileInput").set_input_files("fill_press.py")
    # page.wait_for_timeout(3000)


def test_file_upload_demo_1(page:Page):
    page.goto("http://testautomationpractice.blogspot.com/")

    with page.expect_file_chooser() as file_promise:
        page.locator("id=singleFileInput").click()

    file  = file_promise.value
    file.set_files("fill_press.py")
