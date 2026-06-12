from welcome_page import *
from login import *
def test_login(launch):
    driver = launch
    w=WelcomePage(driver)
    w.logg()
    l=Login(driver)
    l.mail("venkatsoumith@gmail.com")
    l.password("Venky@104")
    l.slogin()