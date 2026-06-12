from time import sleep
class DubaiPackages:
    def __init__(self,driver):
        self.driver=driver
    def view(self):
        sleep(4)
        self.driver.find_element("xpath",
                                 "//h3[contains(.,'Hello Dubai: The Perfect Short Escape')]/ancestor::div//button[contains(.,'View Itinerary')]").click()
    def book(self):
        sleep(4)
        self.driver.find_element("XPATH", "(//button[.='Book now'])").click()
        all_id=self.driver.window_handles
        self.driver.switch_to.window(all_id[1])

