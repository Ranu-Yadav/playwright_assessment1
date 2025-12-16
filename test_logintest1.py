from playwright.sync_api import Page

def test_login1(page:Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
