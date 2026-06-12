class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def email(self,data):
        self.driver.find_element("name","Email").send_keys(data)
    def password(self,data):
        self.driver.find_element("name","Password").send_keys(data)
    def remember(self):
        self.driver.find_element("name","RememberMe").click()
    def login(self):
        self.driver.find_element("xpath","//input[@value='Log in']").click()