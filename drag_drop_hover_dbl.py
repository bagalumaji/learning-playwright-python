from playwright.sync_api import Page


def test_drag_and_drop_demo(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_selector("id=draggable")
    page.locator("id=draggable").drag_to(page.locator("id=droppable"))
    page.wait_for_timeout(5000)