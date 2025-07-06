from playwright.sync_api import Page


def test_frame(page:Page):
    page.goto("https://www.lambdatest.com/selenium-playground/iframe-demo/")
    frame_locator = page.frame_locator("#iFrame1")
    frame_locator.locator("//div[normalize-space()='Your content.']").fill("sayaji bagal")

    # frame1 = page.frame(name="name of frame")
    frame1 = page.frame(url="https://www.lambdatest.com/selenium-playground/iframe-demo/contant")
    frame1.locator("//div[normalize-space()='Your content.']").fill("sharannya bagal")
    page.wait_for_timeout(5000)