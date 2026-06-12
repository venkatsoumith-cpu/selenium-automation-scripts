import pytest
from selenium.webdriver import Chrome
@pytest.fixture
def launch():
    driver = Chrome()
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
