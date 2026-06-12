'''from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//span[.='✕']").click()
driver.find_element("xpath","(//img[contains(@src,'image')])[7]").click()
sleep(2)
#driver.find_element("xpath","(//div[.='My Profile'])[1]").click()
driver.find_element("xpath","(//div[.='Orders'])[1]").click()
sleep(2)
driver.find_element("xpath","//input[@class='c3Bd2c yXUQVt']").send_keys("7036039262")
driver.find_element("xpath","//button[.='Request OTP']").click()
print("otp generated")
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
sleep(2)
a=driver.find_element("id","oldSelectMenu")
s=Select(a)
#s.select_by_index(2)
#s.select_by_value("8")
s.select_by_visible_text("Voilet")
sleep(2)
print(s.is_multiple)'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
sleep(2)
a=driver.find_element("name","cars")
s=Select(a)
s.select_by_index(0)
sleep(2)
s.select_by_value("saab")
sleep(2)
s.select_by_visible_text("Opel")
sleep(2)
s.deselect_all()
print(s.is_multiple)'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
sleep(2)
a=driver.find_element("id","oldSelectMenu")
s=Select(a)
s.select_by_index(0)
sleep(2)
s.select_by_index(1)
sleep(2)
s.select_by_index(2)
b=s.first_selected_option
print(b.text)
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
sleep(2)
a=driver.find_element("name","cars")
s=Select(a)
s.select_by_index(0)
sleep(2)
s.select_by_index(1)
sleep(2)
s.select_by_index(2)
sleep(2)
b=s.first_selected_option
print(b.text)'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","(//div[@class='css-19bb58m'])[3]").click()
sleep(2)
driver.find_element("xpath","//div[.='Black']").click()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.zepto.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//a[@aria-label='Search for products']").click()
sleep(2)
driver.find_element("xpath","//input[@class='flex-1 outline-none']").send_keys("chocolate")
sleep(2)
z=driver.find_elements("xpath","//div[@class='relative']")
for i in z:
    print(i.text)
driver.quit()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)
b=driver.find_element("id","country")
s=Select(b)
sleep(2)
#s.select_by_index(9)
#s.select_by_value("France")
s.select_by_visible_text("France")
print(s.is_multiple)'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)
c=driver.find_element("id","colors")
s=Select(c)
s.select_by_value("red")
sleep(2)
s.select_by_index(2)
sleep(2)
s.select_by_visible_text("Blue")
sleep(2)
b=s.first_selected_option
print(b.text)'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//span[.='✕']").click()
driver.find_element("name","q").send_keys("chocolate")
sleep(2)
f=driver.find_elements("xpath","//div[@class='VDtK0l _1psv1ze2u _1psv1ze53 _1psv1ze9x _1psv1ze7o']")
for i in f:
    print(i.text)'''










