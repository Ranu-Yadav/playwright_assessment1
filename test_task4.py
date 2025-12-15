def test_task4(page):
    page.goto("https://example.com/")

    assert page.get_by_text("This domain is for use in illustrative examples in documents.").is_visible()
