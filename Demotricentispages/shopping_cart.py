from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class ShoppingCart:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def remove1(self):
        remove_btn=self.wait.until(EC.element_to_be_clickable((By.NAME,"removefromcart")))
        remove_btn.click()
    def update_cart(self):
        self.driver.find_element("xpath","//input[@name='updatecart']").click()
