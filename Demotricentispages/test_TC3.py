from welcome_page import *
from shopping_cart import *
def test_testcase3_shopper(launch):
    driver = launch
    w=WelcomePage(driver)
    w.book()
    w.cart1()
    w.shop()
    s=ShoppingCart(driver)
    s.remove1()
    s.update_cart()