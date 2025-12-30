from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("learning")
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.get_by_role("button", name="Sign In").click()
    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    page.locator("app-card").filter(has_text="iphone X $24.99 Lorem ipsum").get_by_role("button").click()
    page.get_by_text("Checkout ( 1 ) (current)").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_role("button", name="Purchase").click()

    # ---------------------
    context.close()
    browser.close()