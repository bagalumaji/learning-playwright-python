from playwright.sync_api import Page


def test_verify_window_handling(page:Page):
    page.goto("https://www.lambdatest.com/selenium-playground/window-popup-modal-demo")
    print(page.title())