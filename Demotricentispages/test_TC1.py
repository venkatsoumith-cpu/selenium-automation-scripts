from welcome_page import *
from register_page import *
def test_testcase1_register(launch):
    driver = launch
    w=WelcomePage(driver)
    w.register()
    r=RegisterPage(driver)
    r.firstname("venkat")
    r.lastname("soumith")
    r.email("venkatsoumith@gmail.com")
    r.password("venky104")
    r.confirm_password("venky104")
    r.Register()
