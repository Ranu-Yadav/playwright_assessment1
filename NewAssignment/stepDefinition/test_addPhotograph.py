import pytest
from pytest_bdd import scenarios, given, when, then, scenario
from playwright.sync_api import expect

from pageObject.addPhotograph import AddPhotograph
from pageObject.login import LoginPage


scenarios("../features/personalDetails.feature")


@given("user is already logged in and My Info page")
def givenUserIsLoggedIn(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = "Admin"
    password = "admin123"
    loginPage = LoginPage(page)
    loginPage.login(username, password)
    try:
        page.get_by_role("button", name="OK").click(timeout=5000)
    except:
        pass
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", timeout=5000)
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    myInfo = page.get_by_text("My Info")
    myInfo.click()
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7", timeout=5000)
    expect(page.get_by_text("heading","Personal Details")).to_be_visible()

@when("user upload image")
def userUploadImage(page):
    image=page.locator("img.employee-image")
    image.click()
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPhotograph/empNumber/7", timeout=5000)
    expect(page.get_by_text("Change Profile Picture")).to_be_visible()
    addPhoto = AddPhotograph(page)
    addPhoto.addPhotograph()

@then("image should be successfully updated")
def imageUploaded(page):
    success_toast = page.get_by_text("Successfully Updated")
    expect(success_toast).to_be_visible()

