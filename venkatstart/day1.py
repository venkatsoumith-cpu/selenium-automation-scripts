'''from selenium.webdriver import Chrome
driver = Chrome()'''
from itertools import product

'''from selenium.webdriver import chrome
c=chrome()'''
'''from selenium.webdriver import Firefox
f=Firefox()'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)'''
'''from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.flipkart.com")
sleep(1)
driver.close()'''
'''from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
eng=driver.find_element("//a[@id='js-link-box-en']")
tooltip=eng.get_attribute("title")
print(tooltip)'''
'''from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com")
driver.maximize_window()
eng=driver.find_element("//a[@aria-label='Google apps']")
tooltip=eng.get_attribute("aria-label")
print(tooltip)'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com")
driver.maximize_window()
sleep(2)
gog=driver.find_element("xpath","//a[@aria-label='Google apps']")
tooltip=gog.get_attribute("aria-label")
print(tooltip)'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.ID,'email').send_keys('selenium@gmail.com')
driver.find_element(By.ID,'pass').send_keys('selenium@123')
driver.find_element(By.NAME,'login').click()'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("file:///C:/Users/venka/OneDrive/Desktop/chvs.html")
driver.maximize_window()
sub = driver.find_element("id", "s1")
s = Select(sub)
s.select_by_index(2)
s.select_by_value("v4")
s.select_by_visible_text("Selenium")'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'email').send_keys('venkatsoumith@gmail.com')
driver.find_element(By.ID,'pass').send_keys('venky104')
sleep(2)
driver.find_element(By.NAME,'pass').send_keys('selenium@123')
sleep(2)
driver.find_element(By.NAME,'login').click()'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.youtube.com/")
driver.maximize_window()
driver.find_element(By.NAME,"search_query").send_keys("python selenium")
driver.find_element(By.CLASS_NAME,"ytSearchboxComponentSearchButton").click()'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://in.bookmyshow.com/explore/home/bengaluru")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"sc-1or3vea-12 dofptW")'''
#ws to verify create account and continue with google is enabled/not in zomato --> signup.
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.zomato.com/bangalore/delivery")
driver.maximize_window()
pizza = driver.find_element(By.CLASS_NAME,"sc-dchYKM onvsl")
print(pizza.text)
if pizza.text == 'Pizza':
    print("Pizza element is present in application")
else:
    print("Pizza element is not present in application")'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Downloads").click()
sleep(1)
driver.find_element(By.LINK_TEXT, "other languages exist").click()
sleep(1)
driver.find_element(By.LINK_TEXT, "Register now!").click()'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("file:///C:/Users/venka/OneDrive/Desktop/chvs.html")
driver.maximize_window()
ops = driver.find_elements("tag name", "a")
for i in ops:
    print(i.text)'''
#ws to click on downloads, other lang exist and register now link in selenium.dev
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Downloads").click()
sleep(3)
driver.find_element(By.LINK_TEXT, "other languages exist").click()
sleep(3)
driver.find_element(By.LINK_TEXT, "Register now!").click()'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("file:///C:/Users/venka/OneDrive/Desktop/chvs.html")
driver.maximize_window()
sub = driver.find_element("id", "s1")
s = Select(sub)
s.select_by_index(2)
sleep(3)
s.select_by_value("v4")
sleep(3)
s.select_by_visible_text("Selenium")'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.vedantu.com/")
driver.maximize_window()
sleep(2)
study = driver.find_element("xpath", "//div[.='Free study material']")
a = ActionChains(driver)
a.move_to_element(study).perform()
sleep(2)
cbse = driver.find_element("xpath", "//h3[.='CBSE']")
a.move_to_element(cbse).perform()
sleep(2)
cbse_notes = driver.find_element("xpath", "//h4[.='CBSE Notes']")
a.move_to_element(cbse_notes).perform()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element("id","twotabsearchtextbox").send_keys("samsung")
sleep(2)
au=driver.find_elements("xpath","//div[@class='s-suggestion s-suggestion-ellipsis-direction']")
for i in au:
    print(i.text)'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//input[@class='desktop-searchBar']").send_keys("lehenga")
sleep(2)
my=driver.find_elements("xpath","//div[@class=' desktop-autoSuggest desktop-showContent']")
for i in my:
    print(i.text)'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.google.com/?hl=te")
driver.maximize_window()
sleep(2)
driver.find_element("name","q").send_keys("python selenium")
sleep(4)
gog=driver.find_elements("xpath","//div[@class='lnnVSe']")
for i in gog:
    print(i.text)'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("http://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
driver.find_element("id","nav-search-submit-button").click()
sleep(2)
parent=driver.current_window_handle
driver.find_element("xpath","(//span[.='97,900'])[1]").click()
sleep(2)
all_id=driver.window_handles
for window in all_id:
    if window !=parent:
        driver.switch_to.window(window)
        print(driver.title)
driver.switch_to.window(parent)
print("Came to parent window")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver .common.keys import Keys
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)
driver.find_element("name","q").send_keys("iphone15",Keys.ENTER)
parent=driver.current_window_handle
driver.find_element("xpath","//li[@class='DTBslk']").click()
sleep(3)
all_id=driver.window_handles
for window in all_id:
    if window !=parent:
        driver.switch_to.window(window)
        print(driver.title)
driver.switch_to.window(parent)
print("Came to parent window")'''






















