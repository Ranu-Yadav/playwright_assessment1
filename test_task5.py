from playwright.sync_api import expect

def test_task5(page):
    page.goto("https://example.com/")

    expect(page).not_to_have_title("new title")

