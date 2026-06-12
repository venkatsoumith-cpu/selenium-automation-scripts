from time import sleep
class RegisterPage:
    def __init__(self,driver):
        self.driver = driver
    def gender(self):
        self.driver.find_element("name","Gender").click()
    def firstname(self,data):
        self.driver.find_element("id","FirstName").send_keys(data)
    def lastname(self,data):
        self.driver.find_element("id","LastName").send_keys(data)
    def email(self,data):
        self.driver.find_element("name","Email").send_keys(data)
    def password(self,data):
        self.driver.find_element("id","Password").send_keys(data)
    def confirm_password(self,data):
        self.driver.find_element("id","ConfirmPassword").send_keys(data)
    def Register(self):
        self.driver.find_element("name","register-button").click()
