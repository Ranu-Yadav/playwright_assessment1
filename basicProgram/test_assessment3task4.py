import time

from playwright.sync_api import Page, expect

def test_frameBreaker(page:Page):
    page.goto("https://the-internet.herokuapp.com/iframe")

    frame = page.frame_locator("#mce_0_ifr")
    editor= frame.locator("#tinymce")

    expect(editor).to_have_attribute("contenteditable","false")

    #frame.keyboard.press("Control+A")
    #frame.keyboard.press("Backspace")

    time.sleep(2)