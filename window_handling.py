from playwright.sync_api import sync_playwright, Page


def test_verify_window_handling():
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

    new_page.close()
    page.close()
    context.close()
    browser.close()
    playwright.stop()

