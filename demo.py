from playwright.sync_api import sync_playwright

def main1():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://google.com")
        url = page.url
        print("url :", url)
        title = page.title()
        print("title :", title)
        page.wait_for_timeout(1000)
        browser.close()

if __name__ == "__main__":
    main1()