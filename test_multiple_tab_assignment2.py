import time

from playwright.sync_api import Playwright, Page, expect


def test_multiple_tab(playwright : Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()

    page.goto("http://seleniumpractise.blogspot.com/2016/08/how-to-use-explicit-wait-in-selenium.html")

    with page.expect_popup() as newPage_info:
        page.get_by_text("Blogger").click()
        childPage = newPage_info.value

    expect(childPage.locator("//h2[text()='Publish your passions, your way']")).to_be_visible()

    page.bring_to_front()

    with page.expect_popup() as newPage1_info:
        page.get_by_text("Blogger").click()
        child1page = newPage1_info.value
        expect(childPage.locator("//h2[text()='Publish your passions, your way']")).to_be_visible()

    page.bring_to_front()
    time.sleep(2)
    childPage.bring_to_front()
    time.sleep(2)
    child1page.bring_to_front()

    time.sleep(2)