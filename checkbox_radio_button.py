from playwright.sync_api import Page


def test_checkbox_radio_button_demo(page:Page):
    page.goto("https://www.lambdatest.com/selenium-playground/checkbox-demo")
    check_locator=page.get_by_label("Click on check box")
    if not check_locator.is_checked():
        check_locator.check()

    page.wait_for_timeout(5000)


