class SignUp:
    def __init__(self,driver):
        self.driver=driver
    def firstname(self,data):
        self.driver.find_element("name","First Name").send_keys(data)
    def lastname(self,data):
        self.driver.find_element("name","Last Name").send_keys(data)
    def gender(self):
        self.driver.find_element("id","Male").click()
    def mobile(self,data):
        self.driver.find_element("id","Phone Number").send_keys(data)
    def email(self,data):
        self.driver.find_element("id","Email Address").send_keys(data)
    def passwrd(self,data):
        self.driver.find_element("name","password").send_keys(data)
    def confirm(self,data):
        self.driver.find_element("name","Confirm Password").send_keys(data)
    def checkbox(self):
        self.driver.find_element("id","Terms and Conditions").click()
    def Registeron(self):
        self.driver.find_element("name","Register").click()