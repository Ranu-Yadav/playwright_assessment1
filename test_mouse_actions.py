import time

from playwright.sync_api import Page

def test_drag_drop(page : Page):
    page.goto("https://jqueryui.com/droppable/")

    frame = page.frame_locator(".demo-frame")

    source = frame.locator("#draggable")
    dest = frame.locator("#droppable")

    source.drag_to(dest)
    time.sleep(5)