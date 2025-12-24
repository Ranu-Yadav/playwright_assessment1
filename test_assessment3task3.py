import time

from playwright.sync_api import Page

def test_keyboard_action(page:Page):
    page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    page.get_by_label("Text input").type("Ranu", delay=500)
    time.sleep(2)
    page.keyboard.press("Tab")
    time.sleep(2)
    page.get_by_label("Password").type("Password", delay=500)
    time.sleep(2)
    page.keyboard.press("Enter")
    time.sleep(2)
    page.goto("https://www.selenium.dev/selenium/web/web-form.html")
    page.get_by_label("Text input").fill("test")
    time.sleep(2)
    page.keyboard.press("Tab")
    time.sleep(2)
    page.get_by_label("Password").fill("test")
    time.sleep(2)
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")

    time.sleep(5)