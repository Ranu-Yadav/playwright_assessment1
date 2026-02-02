from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect
from pageObject.login import LoginPage
from pageObject.personalDetails import PersonalDetails

scenarios("../features/personalDetails.feature")

@given("user is already logged in")
def givenUserIsLoggedIn(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = "Admin"
    password = "admin123"
    loginPage = LoginPage(page)
    loginPage.login(username, password)

@when("user navigate to my profile")
def userNavigateToMyProfile(page):
    try:
        page.get_by_role("button", name="OK").click(timeout=5000)
    except:
        pass
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", timeout=20000)
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    myInfo = page.get_by_text("My Info")
    myInfo.click()

@then("user should be able to view his profile")
def userProfileDetailsVisible(page):
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7", timeout=20000)
    expect(page.get_by_text("Employee Full Name")).to_be_visible()

@when("user update personal details")
def updatePersonalDetails(page, _pytest_bdd_example):
    try:
        page.get_by_role("button", name="OK").click(timeout=5000)
    except:
        pass

    myInfo = page.get_by_text("My Info")
    myInfo.click()
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7", timeout=20000)
    firstName = _pytest_bdd_example["First Name"]
    middleName = _pytest_bdd_example["Middle Name"]
    lastName = _pytest_bdd_example["Last Name"]

    personalDetailsPage = PersonalDetails(page)
    personalDetailsPage.updatePersonalDetails(firstName,middleName,lastName)

@then("successfully updated pop up should come")
def personalDetailsUpdated(page):
    success_toast= page.get_by_text("Successfully Updated")
    expect(success_toast).to_be_visible()