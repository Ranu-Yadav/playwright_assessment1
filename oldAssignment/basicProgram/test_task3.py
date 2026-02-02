def test_task3(page):
    page.goto("https://example.com/")

    title = page.title()
    print(title)

    assert page.get_by_text("Example Domain").is_visible()