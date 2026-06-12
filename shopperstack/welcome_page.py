from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class WelcomePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    def logg(self):
        login_btn=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.='Login']")))
        login_btn.click()