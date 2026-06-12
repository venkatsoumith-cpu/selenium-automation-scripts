import pytest
from selenium.webdriver import Chrome

@pytest.fixture
def run():
    driver = Chrome()
    driver.get("https://pickyourtrail.com/")
    driver.maximize_window()
    driver.implicitly_wait(8)
    yield driver
    driver.quit()


