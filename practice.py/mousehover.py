'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.google.com/?hl=te")
driver.maximize_window()
sleep(2)
m=ActionChains(driver)
#g=driver.find_element("xpath","(//a[.='Gmail'])[1]")
i=driver.find_element("xpath","//a[.='Images']")
m.click(i).perform()
driver.close()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demoqa.com/buttons")
driver.maximize_window()
sleep(2)
a=ActionChains(driver)
d=driver.find_element("id","doubleClickBtn")
a.double_click(d).perform()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.qaplayground.com/practice/buttons")
driver.maximize_window()
sleep(2)
a=ActionChains(driver)
b=driver.find_element("id","btn-double-click")
a.double_click(b).perform()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demoqa.com/buttons")
driver.maximize_window()
sleep(2)
a=ActionChains(driver)
r=driver.find_element("id","rightClickBtn")
a.context_click(r).perform()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.qaplayground.com/practice/buttons")
driver.maximize_window()
sleep(2)
a=ActionChains(driver)
r=driver.find_element("id","btn-right-click")
a.context_click(r).perform()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.amazon.com")
driver.maximize_window()
sleep(2)
m=ActionChains(driver)
a=driver.find_element("xpath","//span[contains(.,'Account & Lists')]")
m.move_to_element(a).perform()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
driver.maximize_window()
sleep(2)
a=ActionChains(driver)
driver.find_element("xpath","//span[@class='ng-tns-c2785778308-3 icon-cancel']").click()
driver.find_element("id","password").send_keys("12345678")
sleep(2)
b=driver.find_element("xpath","(//img[@class='ng-star-inserted'])[1]")
a.click_and_hold(b).perform()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demoapps.qspiders.com/ui/clickHold?sublist=0")
driver.maximize_window()
sleep(2)
a=ActionChains(driver)
q=driver.find_element("id","circle")
a.click_and_hold(q).perform()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
driver.maximize_window()
sleep(2)
a=ActionChains(driver)
driver.find_element("xpath","//span[@class='ng-tns-c2785778308-3 icon-cancel']").click()
driver.find_element("id","password").send_keys("12345678")
sleep(2)
b=driver.find_element("xpath","(//img[@class='ng-star-inserted'])[1]")
a.click_and_hold(b).pause(5).release().perform()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demoapps.qspiders.com/ui/clickHold?sublist=0")
driver.maximize_window()
sleep(2)
a=ActionChains(driver)
r=driver.find_element("id","circle")
a.click_and_hold(r).pause(5).release().perform()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)
a=ActionChains(driver)
source=driver.find_element("id","draggable")
dest=driver.find_element("id","droppable")
a.drag_and_drop(source,dest).perform()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)
a=ActionChains(driver)
b=driver.find_element("id","draggable")
sleep(2)
a.scroll_to_element(b).perform()'''

'''from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.amazon.com")
driver.maximize_window()
sleep(2)
a=ActionChains(driver)
search=driver.find_element("id","twotabsearchtextbox")
search.send_keys("iphone")
sleep(2)
search.clear()
sleep(2)
search.click()
a.key_down(Keys.SHIFT).send_keys("iphone").perform()'''











