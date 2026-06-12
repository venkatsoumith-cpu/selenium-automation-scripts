'''class Testdemo:
    def test_add(self):
      print("addition function")'''
'''class TestSample:
    def test_m1(self):
        print("m1 testcase1")
    def test_m2(self):
        print("m2 testcase2")

class TestSimple:
    def test_m3(self):
        print("m3 testcase1")
    def test_m4(self):
        print("m4 testcase2")'''
from selenium.webdriver import Chrome
'''import pytest
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
def test_trash():
    print("tash testcase")
@pytest.mark.smoke
def test_compose():
    print("compose testcase")
def test_bin():
    print("bin testcase")'''
#pytest filename.py –vs –m “name of the marker”
#from selenium.webdriver import Chrome
'''import pytest
@pytest.fixture
def outer():
    print("check for internet connect")

def test_testcase1(outer):
    print("testcase1")

def test_testcase2(outer):
    print("testcase2")'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
import pytest
@pytest.mark.parametrize("name,email,pwd,mobile",[['venky','soumithvenky@gmail.com','venky104','6302915587'],['sathwik','venkatsatvik007.vs@gmail.com','sathwik123','8106474709']])
def test_naukri_registration(name,email,pwd,mobile):
    driver=Chrome(options=o)
    driver.get("https://www.naukri.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element("xpath","//a[.='Register']").click()
    driver.find_element("id","name").send_keys(name)
    driver.find_element("id","email").send_keys(email)
    driver.find_element("id","password").send_keys(pwd)
    driver.find_element("id","mobile").send_keys(mobile)
    driver.find_element("xpath","//i[@class='ico resman-icon resman-icon-check-box']").click()
    driver.find_element("xpath","//button[.='Register now']").click()'''







