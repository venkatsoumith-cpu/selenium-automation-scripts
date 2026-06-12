
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://pickyourtrail.com/")
driver.maximize_window()
sleep(2)
sub=driver.find_element("xpath","(//button[@value='Holiday Tour Packages'])")
sub.click()
sleep(2)
dubai=driver.find_element("xpath","(//a[contains(.,'Dubai Packages')])")
dubai.click()
driver.implicitly_wait(2)
tour=driver.find_element("xpath","//h3[contains(.,'Hello Dubai: The Perfect Short Escape')]/ancestor::div//button[contains(.,'View Itinerary')]")
tour.click()
driver.implicitly_wait(2)
booking=driver.find_element(By.XPATH,"(//button[.='Book now'])")
booking.click()
driver.implicitly_wait(3)
tooltip=booking.get_attribute("button")
print(tooltip)
driver.implicitly_wait(3)
from_city=driver.find_element(By.XPATH,"//a[.='Bengaluru, BLR']")
from_city.click()
driver.implicitly_wait(2)
date_20=driver.find_element(By.XPATH,"//span[text()='20']")
date_20.click()
driver.implicitly_wait(2)
Adults=driver.find_element(By.XPATH,"//span[text()='2 Adults']")
children=driver.find_element(By.XPATH,"//span[text()='1 Child']")
Adults.click(),children.click()
driver.implicitly_wait(2)
confirm=driver.find_element(By.XPATH,"//button[.='Confirm Changes']")
confirm.click()
driver.implicitly_wait(2)
child_age=driver.find_element(By.XPATH,"//select[@name=='Age of Child 1 as 2 years']")
child_age.click()
driver.implicitly_wait(1)
add_bed=driver.find_element(By.XPATH,"//span[.='Add Extra bed for Child'")
add_bed.click()
driver.implicitly_wait(2)
next_step=driver.find_element(By.XPATH,"//button[.='Next, Select Itinerary']")
next_step.click()
driver.implicitly_wait(2)
mobile=(By.ID,"Enter your mobile number")
sleep(2)
name=(By.ID,"Enter your name")
sleep(2)
view=driver.find_element("XPATH","//button[.='View customized Itinerary]")
view.click()
sleep(2)
language=driver.find_element(By.XPATH,"//span[.='telugu']")
driver.implicitly_wait(2)
all_id=driver.window_handles'''

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.icici.bank.in/")
driver.maximize_window()
wait=WebDriverWait(driver,10)
driver.find_element("xpath","//span[.=' Accounts ']").click()
try:
    block_btn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.='Block']")))
    block_btn.click()
except:
    print("Popup not present")
driver.find_element("xpath","(//a[@type='button'])[2]").click()
sleep(2)
driver.find_element("xpath","//input[@type='text']").send_keys("CHITTAMPALLI VENKAT SOUMITH")
driver.find_element("name","pan").send_keys("CYPPC4341B")
sleep(2)
driver.find_element("name","pincode").send_keys("505001")
driver.find_element("name","mobile").send_keys("6302915585")
sleep(2)
driver.find_element("name","checkbox").click()
driver.find_element("xpath","//button[.='Apply Now']").click()







