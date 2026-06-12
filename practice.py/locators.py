'''from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)
driver.find_element("class name","form-control").send_keys("arbin")'''

'''from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
sleep(2)
driver.find_element("css selector","input[type='text']").send_keys("arbin")
sleep(2)
driver.find_element("css selector","input[data-test='password']").send_keys("123456")
sleep(2)
driver.find_element("css selector","input[id='login-button']").click()'''

'''from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)
driver.find_element("link text","Create new account").click()'''

'''from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(2)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
driver.find_element("id","nav-search-submit-button").click()
sleep(2)
a=driver.find_element("xpath","")
print(a.text)'''

'''from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//span[.='✕']").click()
driver.find_element("name","q").send_keys("iphone",Keys.ENTER)
sleep(2)
f=driver.find_element("xpath","//div[.='Apple iPhone 17 Pro (Silver, 256 GB)']/ancestor::div[@class='col col-7-12']/following-sibling::div//div[.='₹1,26,900']")
print(f.text)'''

'''from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()
sleep(2)
t=driver.find_element("xpath","//td[.='Island Trading']/following-sibling::td")
#t=driver.find_element("xpath","//td[.='Austria']/preceding-sibling::td[1]")
print(t.text)'''

'''from selenium.webdriver import ChromeOptions
from time import sleep
from selenium.webdriver import Chrome
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","(//span[.='Create new account'])[1]").click()
sleep(2)
driver.find_element("xpath","(//div[contains(@class,'xwoeoq')])[1]").click()
sleep(2)
driver.find_element("xpath","//*[.='12']").click()
sleep(2)
driver.find_element("xpath","(//div[contains(@class,'xwoeoq')])[2]").click()
sleep(2)
driver.find_element("xpath","//*[.='September']").click()
sleep(2)
driver.find_element("xpath","(//div[contains(@class,'xwoeoq')])[3]").click()
sleep(2)
driver.find_element("xpath","//*[.='2001']").click()'''

'''from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(2)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
driver.find_element("id","nav-search-submit-button").click()
sleep(2)
driver.find_element("xpath","//span[.='Brands']/../..//i[@class='a-icon a-icon-checkbox']").click()
sleep(2)
n=driver.find_element("xpath","//span[.='Apple iPhone 17 Pro, US Version, 256GB, eSIM, Deep Blue- Unlocked (Renewed)']")
print(n.text)'''

'''from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(2)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
sleep(2)
phone=driver.find_elements("xpath","//div[@class='s-suggestion s-suggestion-ellipsis-direction']")
sleep(2)
for s in phone:
    print(s.text)'''

'''from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//span[.='✕']").click()
driver.find_element("name","q").send_keys("watches")
sleep(2)
w=driver.find_elements("xpath","//div[@class='VDtK0l _1psv1ze2u _1psv1ze53 _1psv1ze9x _1psv1ze7o']")
sleep(2)
for i in w:
    print(i.text)'''

'''from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(2)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
driver.find_element("id","nav-search-submit-button").click()
sleep(2)
driver.find_element("xpath","//h2[.='Apple iPhone 17 Pro, US Version, 256GB, eSIM, Deep Blue- Unlocked (Renewed)']").click()
sleep(2)
driver.back()'''

'''from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//span[.='✕']").click()
driver.find_element("name","q").send_keys("watches",Keys.ENTER)
sleep(2)
parent=driver.current_window_handle
driver.find_element("xpath","(//div[.='₹287'])[1]").click()
sleep(2)
c=child=driver.window_handles
for w in c:
    if w!=parent:
        driver.switch_to.window(w)
        print(driver.title)'''


