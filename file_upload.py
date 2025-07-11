from playwright.sync_api import Page


def test_file_upload_demo(page:Page):
    page.goto("http://testautomationpractice.blogspot.com/")
    page.locator("id=singleFileInput").set_input_files("fill_press.py")
    page.wait_for_timeout(3000)

