'''from xlrd import *
wb=open_workbook("venky.xlsx")
sh=wb.sheet_by_name("Sheet1")
data=sh.row_values(2,0,2)
print(data)'''

'''from xlrd import *
wb=open_workbook("venky.xlsx")
sh=wb.sheet_by_name("Sheet1")
row_count=sh.nrows
print(row_count)
col_count=sh.ncols
print(col_count)'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
from xlrd import *
d={}
wb=open_workbook("venky.xlsx")
sh=wb.sheet_by_name("Sheet1")
row_count=sh.nrows
for i in range(1,row_count):
    data=sh.row_values(i,0,2)
    d[data[0]]=data[1]
for un,pwd in d.items():
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    sleep(2)
    driver.find_element("name", "email").send_keys(un)
    driver.find_element("name", "pass").send_keys(pwd)
    sleep(2)
    driver.find_element("xpath","(//div[.='Log in'])[1]").click()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
import pytest
from xlrd import *
@pytest.mark.parametrize("name, email, pwd, mob", [('amith', 'amithammu1122@gmail.com', 'Amith@123', '9988776655'),
                                                   ('ganesh', 'gavuganesh12@gmail.com', 'GaN#@4546', '9898966778')])
def test_naukri_registeration(name, email, pwd, mob):
    driver = Chrome(options=o)
    driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element("id", "name").send_keys(name)
    driver.find_element("id", "email").send_keys(email)
    driver.find_element("id", "password").send_keys(pwd)
    driver.find_element("id", "mobile").send_keys(mob)
    driver.find_element("xpath", "(//h2[@class='main-3'])[2]").click()
    driver.find_element("xpath","//i[@class='ico resman-icon resman-icon-check-box']").click()
    driver.find_element("xpath", "//button[.='Register now']").click()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
import pytest
from xlrd import *
l=[]
wb = open_workbook("C:\\Users\\venka\\PycharmProjects\\venkatproject\\excel_file\\venky.xlsx")
sh = wb.sheet_by_name("Sheet2")
row_count = sh.nrows
for i in range(1, row_count):
    data = sh.row_values(i)
    l.append(data)
@pytest.mark.parametrize("name, email, pwd, mob", l)
def test_naukri_registeration(name, email, pwd, mob):
    driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element("id", "name").send_keys(name)
    driver.find_element("id", "email").send_keys(email)
    driver.find_element("id", "password").send_keys(pwd)
    driver.find_element("id", "mobile").send_keys(mob)
    driver.find_element("xpath", "(//h2[@class='main-3'])[2]").click()
    driver.find_element("xpath", "//i[@class='ico resman-icon resman-icon-check-box']").click()
    driver.find_element("xpath", "//button[.='Register now']").click()'''












