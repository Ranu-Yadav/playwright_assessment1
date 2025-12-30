import time

from playwright.sync_api import Page, expect


def test_alertboxaccept(page: Page):

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Alert").click()

    time.sleep(5)

def test_alertboxwithokandcancel(page:Page):

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    should_accept = True

    def handle_dialog(dialog):
        if should_accept:
            dialog.accept()
        else:
            dialog.dismiss()

    page.on("dialog", handle_dialog)

    page.locator("#confirmbtn").click()

    time.sleep(5)
    should_accept = False

    page.locator("#confirmbtn").click()
    time.sleep(5)

def test_entertextinalertbox(page: Page):

    page.goto("https://demoqa.com/alerts")

    def handle_dialog(dialog):
        dialog.accept("Ranu")

    page.on("dialog", handle_dialog)

    page.locator("#promtButton").click()
    time.sleep(5)

    expect (page.get_by_text("You entered ranu")).to_be_visible()
    time.sleep(5)