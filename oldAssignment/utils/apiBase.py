from playwright.sync_api import Playwright

class ApiUtils:

    #login to generate token
    def getToken(self, playwright:Playwright):
        loginPayload = {"userEmail": "ranuyadav1401@gmail.com",
                        "userPassword": "Password@1"
                        }
        apirequestcontext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apirequestcontext.post("/api/ecom/auth/login",
                                          data=loginPayload,
                                          headers={
                                              "content-type": "application/json"
                                          })
        #assert response.ok
        response_json= response.json()
        print(response_json)
        return response_json["token"]

    #create order api call
    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)
        #print(token)
        orderPayload = {"orders": [{"country": "India", "productOrderedId": "6960ea76c941646b7a8b3dd5"}]}
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response1 = api_request_context.post(
            "/api/ecom/order/create-order",
            data=orderPayload,
            headers={
                "authorization": token,
                "content-type": "application/json"
            }
        )
        #assert response1.ok
        response_json = response1.json()
        #print(response_json)
        return response_json["orders"][0]


    def getOrderDetails(self, playwright:Playwright, orderId):
        token = self.getToken(playwright)
        apiRequestContext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response2 = apiRequestContext.get("api/ecom/order/get-orders-details",
                                          params={"id": orderId},
                                          headers = {
                                              "authorization": token
                                          })
        orderDetailResponse = response2.json()
        print("printing order details")
        print(orderDetailResponse)
        return orderDetailResponse["data"]
        #return orderDetailResponse["data"]["productName"]


