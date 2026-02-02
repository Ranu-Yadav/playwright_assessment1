def test_task4(page):
    page.goto("https://example.com/")
    assert page.get_by_text("This domain is for use in documentation examples without needing permission.").is_visible()
