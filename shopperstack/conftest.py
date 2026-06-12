import pytest
from selenium.webdriver import Chrome
@pytest.fixture
def launch():
    driver = Chrome()
    driver.get("https://www.shoppersstack.com/")
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


