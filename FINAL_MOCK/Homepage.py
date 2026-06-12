class Homepage:
    def __init__(self,driver):
        self.driver=driver
    def url(self):
        self.driver.get("https://pickyourtrail.com/")
    def tour(self):
        self.driver.find_element("xpath","(//button[@value='Holiday Tour Packages'])")
    def dubai(self):
        self.driver.find_element("xpath","(//a[contains(.,'Dubai Packages')])").click()


