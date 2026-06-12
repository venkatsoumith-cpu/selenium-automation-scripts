from Scripts.runxlrd import options
from selenium.webdriver.common.devtools.v140.pwa import launch

from Homepage import *
from Dubai_packages import *
from Pick import *

def test_dubai_holiday_booking(run):
    driver = run
    h=Homepage(driver)
    h.url()
    h.tour()
    h.dubai()
    c= DubaiPackages(driver)
    c.view()
    c.book()
    b=Pick(driver)
    b.select_Bengaluru("BLR")
    b.select_date20(20)
    b.select_2adults1child()
    b.click_confirmchanges()
    b.selectageofchild1(2)
    b.selectaddextrabed()
    b.clicknextselectitenerary()
    b.entermobilenumber(7036039868)
    b.clickcontinue()
    b.entername("venkat")
    b.view_customised_itenerary('click')
    b.selectlanguage("Telugu")








