import pytest
from playwright.async_api import async_playwright, Page


@pytest.mark.asyncio
async def test_demo_async():
    playwright = await  async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("http://testautomationpractice.blogspot.com/")
    print(await page.title())
    print(page.url)
    await page.get_by_placeholder("Enter Name").fill("Sayaji")
    await page.get_by_placeholder("Enter Email").fill("Sharu@bagal.com")

    await  page.wait_for_timeout(5000)
