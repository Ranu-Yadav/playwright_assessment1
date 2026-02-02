
class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.locator("input[name='username']").fill(username)
        self.page.locator("input[name='password']").fill(password)
        self.page.get_by_role("button").click()

