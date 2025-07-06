from playwright.sync_api import Page


def test_fill_press(page:Page):
    page.goto("https://google.com")
    page.locator("//*[@name='q']").fill("Umaji Bagal")
    page.keyboard.press("Enter")
    # page.wait_for_timeout(10000)
    title = page.title()
    assert "Umaji" in title
