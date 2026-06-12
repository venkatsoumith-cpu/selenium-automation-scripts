from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class DreamPortal_home():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def lanimation(self):
        self.wait.until(EC.invisibility_of_element_located(("id","loadingAnimation")))
    def maincontent_displayed(self):
        return self.driver.find_element("id","mainContent").is_displayed()

    def MyDreams_displayed(self):
       return self.driver.find_element("id","dreamButton").is_displayed()
    def click_mydreams(self):
        self.driver.find_element("id","dreamButton").click()




