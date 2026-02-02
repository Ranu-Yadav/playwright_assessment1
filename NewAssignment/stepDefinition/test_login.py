import pytest
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then

from pageObject.login import LoginPage

scenarios("../features/login.feature")

@given("user is on login page")
def userOnLoginPage(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when("user entered valid {username} and {password}")
def userEnterCreds(page, _pytest_bdd_example):
    username = _pytest_bdd_example["username"]
    password = _pytest_bdd_example["password"]

    loginPage = LoginPage(page)
    loginPage.login(username, password)

@then("user redirected to dashboard page")
def userRedirectToDashboardPage(page):
    try:
        page.get_by_role("button", name="OK").click(timeout=5000)
    except:
        pass
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", timeout=20000)
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    #expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")


@given("user is on login page")
def userOnLoginPage(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when("user entered invalid {username} and valid {password}")
def userEnterCreds(page, _pytest_bdd_example):
    username = _pytest_bdd_example["username"]
    password = _pytest_bdd_example["password"]

    loginPage = LoginPage(page)
    loginPage.login(username, password)

@then("Invalid credentials error will appear")
def checkErrorOnInvalidCreds(page):
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=20000)
    expect(page.get_by_text("Invalid credentials")).to_be_visible()

@given("user is on login page")
def userOnLoginPage(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when("user entered valid {username} and invalid {password}")
def userEnterCreds(page, _pytest_bdd_example):
    username = _pytest_bdd_example["username"]
    password = _pytest_bdd_example["password"]

    loginPage = LoginPage(page)
    loginPage.login(username, password)

@then("Invalid credentials error will appear")
def checkErrorOnInvalidCreds(page):
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=20000)
    expect(page.get_by_text("Invalid credentials")).to_be_visible()

@given("user is on login page")
def userOnLoginPage(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when("user entered invalid {username} and invalid {password}")
def userEnterCreds(page, _pytest_bdd_example):
    username = _pytest_bdd_example["username"]
    password = _pytest_bdd_example["password"]

    loginPage = LoginPage(page)
    loginPage.login(username, password)

@then("Invalid credentials error will appear")
def checkErrorOnInvalidCreds(page):
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=20000)
    expect(page.get_by_text("Invalid credentials")).to_be_visible()