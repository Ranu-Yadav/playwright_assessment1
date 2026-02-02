import time
import json
import pytest
from playwright.sync_api import Playwright, expect
from oldAssignment.utils.apiBase import ApiUtils
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "userCredential.json"

with open(DATA_FILE) as f:
    test_data= json.load(f)
    print(test_data)
    user_credential_data = test_data["user_credentials"]
@pytest.mark.parametrize("user_credential", user_credential_data)
def test_UIandAPIscript(playwright: Playwright, user_credential):

    userName = user_credential["userName"]
    password = user_credential["password"]


    #api call to get order id
    apiutils= ApiUtils()
    orderId = apiutils.createOrder(playwright)
    orderdetailsData = apiutils.getOrderDetails(playwright, orderId)
    print(orderdetailsData)

    #check orderid in UI
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.locator("#userEmail").fill(userName)
    page.locator("#userPassword").fill(password)
    page.locator("#login").click()

    page.get_by_role("button", name="ORDERS").click()
    row= page.locator("tr").filter(has_text=orderId)
    expect(row).to_be_visible()

    #check order details in UI
    page.get_by_role("button", name="View").click()


    time.sleep(2)
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="Delete").click()
    expect(page.get_by_text("You have No Orders to show at this time")).to_be_visible()
    time.sleep(2)
