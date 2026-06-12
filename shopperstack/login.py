class Login():
    def __init__(self,driver):
        self.driver=driver
    def create(self):
        self.driver.find_element("xpath","//span[.='Create Account']").click()
    def mail(self,data):
        self.driver.find_element("name","Email").send_keys(data)
    def password(self,data):
        self.driver.find_element("id","Password").send_keys(data)
    def slogin(self):
        self.driver.find_element("xpath","//span[.='Login']").click()
