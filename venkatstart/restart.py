
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
mail=driver.find_element(By.XPATH,"//input[@name='email']")
mail.send_keys("selenium")
mail.clear()
mail.send_keys("Pythonselenium")
driver.close()'''
from time import sleep

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.naukri.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//a[.='Register']").click()
login=driver.find_element(By.XPATH,"//button[.='Register now']")
print(login.is_enabled())
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("file:///C:/Users/venka/OneDrive/Desktop/sample.html")
driver.maximize_window()
sleep(2)
#link1=driver.find_element("id","l1")
#print(link1.is_displayed())
link2=driver.find_element("id","l2")
print(link2.text)
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
gog=driver.find_element(By.XPATH,"//a[@aria-label='Google apps']")
tooltip=gog.get_attribute("aria-label")
print(tooltip)
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.wipro.com/")
driver.maximize_window()
about = driver.find_element("xpath", "(//a[contains(., 'About')])[1]")
print(about.text)
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("file:///C:/Users/venka/OneDrive/Desktop/Untitled2.html")
driver.maximize_window()
sleep(2)
ssd=driver.find_element("id","s1")
s=Select(ssd)
s.select_by_index(0)
s.select_by_visible_text("Selenium")
s.select_by_value("v4")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("file:///C:/Users/venka/OneDrive/Desktop/Untitled2.html")
driver.maximize_window()
sleep(2)
msd=driver.find_element("id","s2")
s=Select(msd)
s.select_by_index(1)
s.select_by_visible_text("Query")
s.select_by_value("v44")
sleep(2)
s.deselect_by_index(3)
s.deselect_by_value("v11")
s.deselect_by_visible_text("Scripts")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"(//span[.='Create new account'])[2]").click()
sleep(2)
driver.find_element(By.XPATH,"(//div[.='Day'])[1]/descendant::div[2]").click()
sleep(2)
driver.find_element(By.XPATH,"(//div[.='Month'])[1]/descendant::div[2]").click()
sleep(2)
driver.find_element(By.XPATH,"(//div[.='Year'])[1]/descendant::div[1]").click()
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("file:///C:/Users/venka/OneDrive/Desktop/Untitled2.html")
driver.maximize_window()
sleep(2)
#ssd=driver.find_element("id","s1")
msd=driver.find_element("id","s2")
#s1=Select(ssd)
top=Select(msd)
top.select_by_index(0)
top.select_by_index(2)
top.select_by_index(3)
ops=top.all_selected_options
for i in ops:
    print(i.text)
#s2=Select(msd)
#print(s2.is_multiple)
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
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
cbse = driver.find_element("xpath","(//a[.='CBSE'])[1]")
a.move_to_element(cbse).perform()
sleep(2)
cbse_notes = driver.find_element("xpath", "//h4[.='CBSE Notes']")
a.move_to_element(cbse_notes).perform()
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://pschool.in/science-3-sc/drag-drop-organs")
driver.maximize_window()
sleep(2)
src1 = driver.find_element("xpath", "(//div[.='Brain'])[1]")
dest1 = driver.find_element("xpath", "(//div[@class='blank '])[1]")
a = ActionChains(driver)
a.drag_and_drop(src1, dest1).perform()
sleep(2)
src2 = driver.find_element("xpath", "(//div[.='Heart'])[1]")
dest2 = driver.find_element("xpath", "(//div[@class='blank '])[2]")
a.drag_and_drop(src2, dest2).perform()
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
sleep(2)
double = driver.find_element("xpath", "//button[.='Double-Click Me To See Alert']")
a = ActionChains(driver)
a.double_click(double).perform()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.select import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.google.com/?hl=te")
driver.maximize_window()
sleep(2)
right=driver.find_element("xpath","(//a[.='Gmail'])[1]")
a=ActionChains(driver)
a.context_click(right).perform()
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)
mail=driver.find_element(By.XPATH,"//input[@name='email']")
Pass=driver.find_element(By.XPATH,"//input[@type='password']")
mail.send_keys("selenium")
sleep(2)
#mail.send_keys(Keys.CONTROL+"a")
mail.send_keys(Keys.CONTROL+"c")
Pass.send_keys(Keys.CONTROL+"v")
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.decathlon.in/")
driver.maximize_window()
sleep(2)
for i in range(0,3):
        driver.execute_script("window.scrollBy(0, 500)")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(2)
sun=driver.find_element("xpath","//h3[.='Get the perfect shape - Sunglasses']")
s=sun.location
driver.execute_script(f"window.scrollBy({s['x']},{s['y']})")
sleep(2)
ele = driver.find_element("xpath", "//img[@title='Online_Eye_Test_desktop']")
d = ele.location
driver.execute_script(f"window.scrollTo({d['x']}, {d['y']})")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//input[@value='Search']").click()
#driver.find_element("xpath","//button[.='English']").click()
#driver.find_element("xpath", "//a[@title='Login']").click()
a = driver.switch_to.alert
print(a.text)'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://abhibus.com")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//span[.='Login/SignUp']").click()
sleep(2)
driver.find_element("xpath","(//input[@type='text'])[4]").send_keys("6302915586")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://mamaearth.in/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//div[.='Login']").click()
sleep(2)
driver.find_element("xpath","//input[@placeholder='Mobile number']").send_keys("6302915586")
sleep(2)
driver.find_element("xpath","//button[.='Login with OTP']").click()'''


'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","(//h2[@class='main-3'])[1]").click()
sleep(2)
driver.find_element("xpath","//button[.='Upload Resume']").click()
sleep(2)
driver.find_element("xpath","//input[@type='file']").send_keys(r"C:\\Users\\venka\\Downloads\\fireflink_mock_interview.pdf")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.shine.com/registration/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//input[@type='file']").send_keys(r"C:\\Users\\venka\\OneDrive\\Desktop\\Complete Tutorial\\Manual Testing\\Types of environment1.docx")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
sleep(2)
driver.find_element("xpath", "//a[.='Twitter']").click()
sleep(2)
driver.find_element("xpath", "//a[.='Google+']").click()
sleep(2)
#cw=driver.current_window_handle
#print(cw)
acp=driver.window_handles
print(acp)
for i in acp[1:]:
    driver.switch_to.window(i)
    sleep(3)
    driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("file:///C:/Users/venka/OneDrive/Desktop/parent.html")
driver.maximize_window()
sleep(2)
un1=driver.find_element("id","a1")
un1.send_keys("hello")
sleep(2)
frame1=driver.find_element("xpath","//iframe[@id='f1']")
driver.switch_to.frame(frame1)
un2=driver.find_element("id","a2")
un2.send_keys("bye")
sleep(2)
frame2=driver.find_element("xpath","//iframe[@id='f2']")
driver.switch_to.frame(frame2)
un3=driver.find_element("id","a3")
un3.send_keys("good")
sleep(2)
driver.switch_to.default_content()
un1.send_keys("Back to main parent")
driver.close()'''

'''assert 10==10,"number not matches"
print("same")
print("end")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
filepath=f("C:\\Users\\venka\\PycharmProjects\\venkatproject\\venkatstart\\New folder")
driver.get("https://www.redbus.in/")
driver.maximize_window()
sleep(2)
driver.save_screenshot(f"{filepath}\\defect1.png")'''

'''from datetime import datetime
d=datetime.now()
print(d)
d=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(d)'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
file=f"C:\\Users\\venka\\PycharmProjects\\venkatproject\\venkatstart\\New folder"
d=datetime.now().strftime("%d-%m-%Y %H-%M-%S")
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
driver.save_screenshot(f"{file}\\{d}.png")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.instagram.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("name","email").send_keys("selenium")
driver.find_element("xpath","//input[@type='password']").send_keys("selenium@123")
driver.find_element("xpath","(//div[.='Log in'])[1]").click()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("xpath","//a[.='Facebook']").click()
tts=driver.window_handles
driver.switch_to.window(tts[1])
wait=WebDriverWait(driver,10)
#wait.until(lambda driver: "Facebook" in driver.title and "NopCommerce" in driver.title)
wait.until(EC.url_contains("https://www.facebook"))
print("Verification")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located(("xpath","(//a[contains(.,'Books')])[1]")))
print("Element is visible in webpage")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.dmartindia.com/")
driver.maximize_window()
wait=WebDriverWait(driver,10)
wait.until(EC.text_to_be_present_in_element(("xpath","(//span[@class='MuiButton-label'])[2]"),"CATEGORIES"))
print("Text in element is present")'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.dom_storage import clear
from selenium.webdriver.support.ui import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.walmart.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10, poll_frequency=1)'''












































































