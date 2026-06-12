class WelcomePage():
    def __init__(self,driver):
        self.driver = driver
    def register(self):
        self.driver.find_element("xpath","//a[.='Register']").click()
    def login(self):
        self.driver.find_element("xpath","//a[.='Log in']").click()
    def book(self):
        self.driver.find_element("xpath","(//a[contains(.,'Books')])[3]").click()
    def cart1(self):
        self.driver.find_element("xpath","(//input[@class='button-2 product-box-add-to-cart-button'])[1]").click()
    def shop(self):
        self.driver.find_element("xpath","(//span[@class='cart-label'])[1]").click()