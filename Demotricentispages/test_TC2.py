from welcome_page import *
from login_page import *
def test_TC2_logging(launch):
    driver = launch
    w=WelcomePage(driver)
    w.login()
    l=LoginPage(driver)
    l.email("venkatsoumith@gmail.com")
    l.password("venky104")
    l.remember()
    l.login()



