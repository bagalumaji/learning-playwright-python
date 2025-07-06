from playwright.sync_api import Page


def test_verify_selection_option(page:Page):
    page.goto("https://www.lambdatest.com/selenium-playground/select-dropdown-demo")
    drp = page.locator("#select-demo")
    drp.select_option("Sunday")
    print("title : "+page.title())
    page.wait_for_timeout(1000)
    print("selected value : "+drp.input_value())
    drp.select_option(label="Saturday")
    page.wait_for_timeout(1000)
    print("selected value : "+drp.input_value())
    drp.select_option(index=3)
    page.wait_for_timeout(1000)
    print("selected value : "+drp.input_value())
    drp1 = page.locator("#multi-select")
    drp1.select_option(value=["Florida"],index=[6],label=["New Jersey"])
    selected_values = page.locator("#multi-select").evaluate("el => Array.from(el.selectedOptions).map(option => option.text)")
    print(selected_values)

    # page.wait_for_timeout(5000)


