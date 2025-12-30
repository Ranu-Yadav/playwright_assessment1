import time

from playwright.sync_api import Page

def test_mouse_action(page : Page):
    #below code is for drag and drop
    page.goto("https://jqueryui.com/droppable/")

    frame = page.frame_locator(".demo-frame")

    source = frame.locator("#draggable")
    dest = frame.locator("#droppable")

    source.drag_to(dest)
    time.sleep(1)

    # below code is for move box from one place to another
    page.goto("https://jqueryui.com/draggable/")

    box = frame.locator("#draggable")

    box_detail = box.bounding_box()

    if not box_detail:
        raise Exception("could not find box")

    start_x = box_detail["x"]+box_detail["width"]/2
    start_y = box_detail["y"]+box_detail["height"]/2

    page.mouse.move(start_x, start_y)
    page.mouse.down()

    time.sleep(2)

    page.mouse.move(start_x + 100, start_y + 100 , steps=25)
    page.mouse.up()

    time.sleep(2)

    #below code is for resizable

    page.goto("https://jqueryui.com/resizable/")

    resize1 = frame.locator("#resizable")

    resize_box = resize1.bounding_box()

    if not resize_box:
        raise Exception("could not find box")
    start_i = resize_box["x"]
    start_j = resize_box["y"]

    page.mouse.dblclick(start_i, start_j)
    page.mouse.down()
    time.sleep(2)

    page.mouse.dblclick(start_i+500, start_j+500)
    page.mouse.up()

    time.sleep(2)
