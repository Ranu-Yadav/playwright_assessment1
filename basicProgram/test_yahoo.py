import time

from playwright.sync_api import Page

def test_yahookeyboardaction(page:Page):
    page.goto("https://login.yahoo.com/account/create")
    page.get_by_label("First Name").type("Ranu", delay=200)
    page.keyboard.press("Tab")
    page.get_by_label("Last Name").type("Yadav", delay=200)
    page.keyboard.press("Tab")
    page.get_by_label("New Yahoo email").type("testthisemail", delay=150)
    #time.sleep(5)
    page.close()


