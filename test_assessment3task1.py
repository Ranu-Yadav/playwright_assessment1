import time

from playwright.sync_api import Page, expect


def test_dialogtamer_accept(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()
    expect(page.get_by_text("You successfully clicked an alert")).to_be_visible()

    time.sleep(3)

def test_dialogtamer_dismiss(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.dismiss())

    page.get_by_role("button", name="Click for JS Confirm").click()

    expect(page.get_by_text("You clicked: Cancel")).to_be_visible()

    time.sleep(3)

def test_dialogtamer_text(page:Page):

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.accept("Playwright Hero"))

    page.get_by_role("button", name="Click for JS Prompt").click()

    expect(page.get_by_text("You entered: Playwright Hero")).to_be_visible()

    time.sleep(3)
