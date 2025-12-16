from playwright.sync_api import Page

def test_login(page:Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username" , "student")
    page.fill("#password" , "Password123")