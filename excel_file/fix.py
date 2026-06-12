from time import sleep
import pytest
''''@pytest.mark.parametrize("a",[10,20,30,40])
def test_add(a):
    print(f"input is {a}")'''
''''@pytest.mark.parametrize("a,b",[[10,20],[2,8],[8,4]])
def test_add(a,b):
    print(f"result is : {a+b}")'''
''''@pytest.mark.parametrize("a,b,c",[[10,20],[2,8],[8,4]])
def test_add(a,b,c):
    print(f"result is : {a+b+c}")'''
'''class Test_Demo:
    @pytest.mark.parametrize(["a", "b"], [["hey", "bye"], ["class", "over"]])
    def test_tc1(self, a, b):
        print(a, b)'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep
from selenium.webdriver.common.keys import Keys
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
@pytest.mark.parametrize("un, pwd", [["venkatsoumith", "venky@104"],
                                     ["mahesh", "mahesh@12123"],
                                     ["kumar", "kumar@!2334"]])
def test_login(un, pwd):
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element("name","email").send_keys(un)
    driver.find_element("name","pass").send_keys(pwd)
    driver.find_element("xpath","(//div[.='Log in'])[1]").click()'''

''''@pytest.fixture
def outer():
    print("check for internet connect")
    yield
    print("off internet")
def test_testcase1(outer):
    print("testcase1")
def test_testcase2(outer):
    print("testcase2")'''
''''@pytest.fixture
def outer1():
    print("check for internet connection")
    yield
    print("off internet")
@pytest.fixture
def outer2():
    print("check for server connection")
    yield
    print("off server")
@pytest.mark.smoke
def test_testcase1(outer1, outer2):
    print("testcase1")
def test_testcase2(outer1, outer2):
    print("testcase2")'''
''''@pytest.fixture(scope="class", autouse=True)
def install():
    print("install build")
    yield
    print("uninstall build")
class Test_Insta:
    def test_login(self):
        print("testcase on login")

    def test_signup(self):
        print("testcase on signup")
class Test_FB:

    def test_reels(self):
        print("testcase on reels")
    def test_story(self)
        print("testcase on story")'''
'''pytestmark = pytest.mark.usefixtures("setup")
@pytest.fixture(scope="module")
def setup():
    print("before")
    yield
    print("end")
def test_tc1():
    print("tescase1")
class Test_FB:
    def test_reels(self):
        print("testcase on reels")
    def test_story(self):
        print("testcase on story")'''
''''@pytest.fixture(autouse=True)
def greet():
    print("welcome")
    yield
    print("end")
def test_TC1():
    print("testcase1")
def test_TC2():
    print("testcase2")
def test_TC3():
    print("testcase3")'''
''''@pytest.fixture
def fix1():
    print("start1")
@pytest.fixture
def fix2():
    print("start2")
def test_tc1(fix1,fix2):
    print("testcase1")'''
''''@pytest.fixture(autouse=True,scope="class",params=["id1","id2"])
def wish():
    print("welcome")
    yield
    print("end")
class Test_Insta:
    def test_tc2(self):
        print("testcase2")
    def test_tc3(self):
        print("testcase3")'''
''''@pytest.fixture(autouse=True, params=["id1", "id2"])
def wish(request):
    print("welcome")
    print(f"the input is {request.param}")
def test_tc2():
    print("testcase2")
def test_tc3():
    print("testcase3")'''
''''@pytest.fixture(autouse=True, params=[4563, 6745, 2345, 7812, 1234])
def wish(request):
    print("welcome")
    if request.param<3000:
        print(f"the ID-{request.param} for regression")
def test_tc2():
    print("testcase2")
def test_tc3():
    print("testcase3")'''
''''@pytest.fixture(params=[["demo","demo@123"], ["sample", "sample@123"], ["log", "log@123"]])
def wish(request):
    print("Welcome")
    print(request.param)
    yield
    print("End")
def test_tc1(wish):
    print("Testcase1")'''
''''@pytest.fixture(params=[["demo","demo@123"], ["sample", "sample@123"], ["log", "log@123"]])
def wish(request):
    if len(request.param[0])>=4:
        print("Welcome")
        print(f"Valid username is {request.param[0]}")
    yield
    print("End")
def test_tc1(wish):
    print("Testcase1")'''
''''@pytest.fixture(params=["mozila", "chrome", "ie"])
def wish(request):
    print("welcome")
    yield request.param
def test_tc1(wish):
    a = wish
    print(a)
    print("testcase1")'''
''''@pytest.fixture
def wish():
    ip = "123.567.678.0.0"
    print("welcome")
    yield ip
def test_tc1(wish):
    ip = wish
    print(ip)
    print("testcase1")'''
'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
@pytest.fixture
def launch():
    driver=Chrome(options=o)
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
    driver.find_element("xpath","//i[.='Search']").click()
    driver.find_element("xpath","(//span[.='Log in'])[1]").click()
    driver.find_element("name","wpName").send_keys("selenium")
    driver.find_element("name","wpPassword").send_keys("selenium@123")
    driver.find_element("xpath","//button[.='Log in']").click()

def test_tc3(launch):
    driver=launch
    driver.find_element("xpath","//i[.='Search']").click()
    driver.find_element("xpath","(//span[.='Create account'])[1]").click()
    driver.find_element("name","wpName").send_keys("pyselenium")
    driver.find_element("name","wpPassword").send_keys("pyselenium@123")
    driver.find_element("name","retype").send_keys("pyselenium@123")
    driver.find_element("name","email").send_keys("selenium@gmail.com")
    driver.find_element("name","wpCreateaccount").click()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
from selenium.webdriver import Firefox,Edge
@pytest.fixture(params=["chrome","firefox","edge"])
def launch(request):
    if request.param == "chrome":
        driver = Chrome(options=o)
    elif request.param == "firefox":
        driver = Firefox()
    else:
        driver = Edge()
    driver.get("https://www.wikipedia.org/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
def test_TC1(launch):
    driver = launch
    driver.find_element("xpath", "//strong[.='English']").click()
    driver.find_element("xpath", "//span[.='View history']").click()
    driver.find_element("xpath", "//span[.='Talk']").click()'''



















