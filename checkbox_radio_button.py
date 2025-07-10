from playwright.sync_api import Page


def test_checkbox_demo(page:Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    check_locator_1=page.locator("(//input)[1]")
    check_locator_2=page.locator("(//input)[2]")
    print(check_locator_1.is_checked())
    print(check_locator_2.is_checked())
    if not check_locator_1.is_checked():
        check_locator_1.check()

    if not check_locator_2.is_checked():
        check_locator_2.check()

    # page.wait_for_timeout(5000)

def test_radio_button_demo(page):
    page.goto("https://demo.automationtesting.in/Register.html")
    radio_locator = page.get_by_label("Male",exact=True)
    print(radio_locator.is_checked())
    if not radio_locator.is_checked():
        radio_locator.check()

    page.wait_for_timeout(5000)
