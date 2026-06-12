from selenium.webdriver.common.by import By
class SummaryPage:
    def __init__(self, driver):
        self.driver = driver
    def get_page_text(self):
        return self.driver.find_element(By.TAG_NAME,"body").text
    def summary_text(self):
        return self.driver.find_element(By.TAG_NAME,"body").text
