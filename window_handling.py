from playwright.sync_api import sync_playwright, Page
from pytest_playwright.pytest_playwright import browser


def te1st_verify_window_handling():
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(headless=False,channel="chrome")
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.lambdatest.com/selenium-playground/window-popup-modal-demo")
    print(page.title())

    page.locator("//a[normalize-space()='Follow On Twitter']").wait_for(state="visible", timeout=10000)

    page.locator("//a[normalize-space()='Follow On Twitter']").click(force=True)

    new_page = context.wait_for_event("page")
    new_page.wait_for_load_state()
    print(new_page.title())

    # new_page.close()
    # page.close()
    context.close()
    browser.close()
    playwright.stop()


def test_window_handling_demo_1():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page_1 = context.new_page()
    page_1.goto("http://testautomationpractice.blogspot.com/")

    with context.expect_page() as page_promise:
        page_1.locator("id=PopUp").click()

    page_2 = page_promise.value
    print(page_2.title())
    print(page_2.url)

    page_2.wait_for_timeout(10000)
    page_2.close()
    page_1.close()
    playwright.stop()