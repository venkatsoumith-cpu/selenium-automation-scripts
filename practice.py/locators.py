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
'''import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
@pytest.mark.parametrize("name,email,pwd,mob",[['amith','amithammu1122@gmail.com','Amith@123','9988776655'],['ganesh','gavuganesh12@gmail.com','Gan#@4546','9898966778']])
def test_naukri_registration(name,email,pwd,mob):
    driver=Chrome(options=o)
    driver.get("https://www.naukri.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element("xpath","//a[.='Register']").click()
    driver.find_element(By.ID,'name').send_keys(name)
    driver.find_element(By.ID,'email').send_keys(email)
    driver.find_element(By.ID,'password').send_keys(pwd)
    driver.find_element(By.ID,'mobile').send_keys(mob)
    driver.find_element("xpath","(//h2[@class='main-3'])[2]").click()
    driver.find_element("xpath","//i[@class='ico resman-icon resman-icon-check-box']").click()
    driver.find_element("xpath","//button[.='Register now']").click()'''

'''import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
@pytest.mark.parametrize("un,pwd",[["venkatsoumith","venky@104"],["mahesh","mahesh@12123"],["kumar","kumar@12334"]])
def test_login(un,pwd):
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.NAME,'email').send_keys(un)
    driver.find_element(By.NAME,'pass').send_keys(pwd)
    driver.find_element("xpath","(//div[.='Log in'])[1]").click()'''

'''import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
@pytest.fixture
def launch():
    driver = Chrome(options=o)
    driver.get("https://www.wikipedia.org/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
def test_tc1(launch):
    driver=launch
    driver.find_element("xpath","//strong[.='English']").click()
    driver.find_element("xpath","(//span[.='View history'])[1]").click()
    driver.find_element("xpath","//span[.='Talk']").click()
def test_tc2(launch):
    driver=launch
    driver.find_element("xpath","//i[@class='sprite svg-search-icon']").click()
    driver.find_element("xpath","(//span[.='Log in'])[1]").click()
    driver.find_element(By.ID,'wpName1').send_keys("venky@104")
    driver.find_element(By.ID,'wpPassword1').send_keys("12345")
    driver.find_element("xpath","//button[.='Log in']").click()
def test_tc3(launch):
    driver=launch
    driver.find_element("xpath","//strong[.='English']").click()
    driver.find_element("xpath","(//span[.='Create account'])[1]").click()
    driver.find_element(By.ID,'wpName2').send_keys("venky@104")
    driver.find_element(By.ID,'wpPassword2').send_keys("12345")
    driver.find_element(By.ID,'wpRetype').send_keys("12345")
    driver.find_element(By.ID,'wpEmail').send_keys("chvs@gmail.com")
    driver.find_element("xpath","//button[.='Create your account']").click()'''

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath","//a[.='Register']").click()
sleep(2)
driver.find_element("id","gender-male").click()
driver.find_element("id","FirstName").send_keys("salman")
driver.find_element("id","LastName").send_keys("shaik")
driver.find_element("name","Email").send_keys("salmanshaik@gmail.com")
driver.find_element("id","Password").send_keys("123456")
driver.find_element("id","ConfirmPassword").send_keys("123456")
driver.find_element("id","register-button").click()
driver.quit()











