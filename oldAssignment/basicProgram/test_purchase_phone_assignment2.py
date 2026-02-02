import time

from playwright.sync_api import Playwright, Page, expect


def test_verify_cart_value(playwright : Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("checkbox").check()
    page.locator("#signInBtn").click()

    phone1 = "iphone X"
    phone2 = "Nokia Edge"

    iphoneLocator = page.locator("app-card").filter(has_text=phone1)
    iphoneLocator.get_by_role("button").click()

    nokiaLocator = page.locator("app-card").filter(has_text=phone2)
    nokiaLocator.get_by_role("button").click()

    page.get_by_text("Checkout").click()

    expect(page.locator(".media-body")).to_have_count(2)

    expect(page.locator(".media-body")).to_contain_text([
        "iphone X",
        "Nokia Edge"
    ])
    page.get_by_text("Checkout").click()

    page.get_by_role("button", name="Purchase").click()

    expect(page.get_by_text("Thank you! Your order will be delivered in next few weeks"))

    time.sleep(5)