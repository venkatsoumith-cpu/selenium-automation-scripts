from selenium.webdriver.common.by import By
class DiaryPage:
    Rows=(By.XPATH,"//table/tbody/tr")
    def __init__(self, driver):
        self.driver = driver
    def get_rows(self):
        return self.driver.find_elements(*self.Rows)