class PersonalDetails:

    def __init__(self, page):
        self.page=page

    def updatePersonalDetails(self, firstName, middleName, lastName):
        self.page.get_by_placeholder("First Name").fill(firstName)
        self.page.get_by_placeholder("Middle Name").fill(middleName)
        self.page.get_by_placeholder("Last Name").fill(lastName)

        saveLocator = self.page.get_by_role("heading",name= "Personal Details").locator("..")
        saveLocator.get_by_role("button", name="Save").click()


