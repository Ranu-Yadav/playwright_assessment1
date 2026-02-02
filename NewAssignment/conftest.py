import pytest
"""
@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

"""

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", choices=["chrome","firefox"], help="browser selection"
    )
    parser.addoption(
        "--url",
        action="store",
        #default="https://google.com",
        help="url to open"
    )

@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    url = request.config.getoption("--url")
    print(url)

    if browser_name == "chrome":
        browser= playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError("unsupported browser name, please enter chrome or firefox")

    context = browser.new_context()
    page = context.new_page()

    yield page
    context.close()
    browser.close()
