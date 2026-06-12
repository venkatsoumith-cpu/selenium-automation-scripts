from welcome_page import *
from login import *
from signup import *
def test_create(launch):
    driver=launch
    w=WelcomePage(driver)
    w.logg()
    l=Login(driver)
    l.create()
    s=SignUp(driver)
    s.firstname("venkat")
    s.lastname("sathwik")
    s.gender()
    s.mobile("8106474707")
    s.email("venkatsatvik007.vs@gmail.com")
    s.passwrd("Sathwik123")
    s.confirm("Sathwik123")
    s.checkbox()
    s.Registeron()


