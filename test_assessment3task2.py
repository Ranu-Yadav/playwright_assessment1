import time

from playwright.sync_api import Page, expect

def test_handlemouseevent1(page:Page):
    page.goto("https://demoqa.com/buttons")

    page.get_by_role("button", name="Double Click Me").dblclick()
    expect(page.get_by_text("You have done a double click")).to_be_visible()
    time.sleep(2)

def test_handlemouseevent2(page: Page):
    page.goto("https://demoqa.com/buttons")
    page.get_by_role("button", name="Right Click Me").click(button="right")
    expect(page.get_by_text("You have done a right click")).to_be_visible()
    time.sleep(2)

def test_handlemouseevent3(page: Page):
    page.goto("https://demoqa.com/buttons")
    page.mouse.move(100, 200)
    page.get_by_role("button", name="Click Me", exact=True).click()
    time.sleep(2)