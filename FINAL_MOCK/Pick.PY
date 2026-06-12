from time import sleep
from selenium.webdriver.common.by import By
class Pick:
    def __init__(self,driver):
        self.driver=driver
    def city(self):
        sleep(4)
        self.driver.find_element("XPATH","//a[.='Bengaluru, BLR']").click()
    def date(self):
        self.driver.find_element("XPATH","//span[text()='20']").click()
    def adult(self):
        sleep(2)
        self.driver.find_element("XPATH","//span[text()='2 Adults']")
    def children(self):
        self.driver.find_element("XPATH","//span[text()='1 Child']").click()
        sleep(2)
    def confirm(self):
        self.driver.find_element("XPATH","//button[.='Confirm Changes']").click()
    def select(self):
        sleep(4)
        self.driver.find_element("XPATH","//select[@name=='Age of Child 1 as 2 years']").click()
    def extra(self):
        self.driver.find_element("XPATH","//span[.='Add Extra bed for Child'").click()
    def next(self):
        self.driver.find_element("XPATH","//button[.='Next, Select Itinerary']").click()
    def mobile(self):
        sleep(4)
        self.driver.find_element(By.ID,"Enter your mobile number")
    def name(self):
        self.driver.find_element(By.ID,"Enter your name")
    def custom(self):
        self.driver.find_element("XPATH","//button[.='View customized Itinerary]")
    def language(self):
        sleep(4)
        self.driver.find_element("XPATH","//span[.='telugu']")
        all_id = self.driver.window_handles
        self.driver.switch_to.window(all_id[2])


