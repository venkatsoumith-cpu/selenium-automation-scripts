from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://arjitnigam.github.io/myDreams/")
driver.maximize_window()
wait=WebDriverWait(driver,10)
wait.until(EC.invisibility_of_element_located(("id","loadingAnimation")))
main_content=driver.find_element("id","mainContent")
assert main_content.is_displayed()
print("Loading animation completed successfully")
my_dreams=driver.find_element("id","dreamButton")
assert my_dreams.is_displayed()
print("My dreams button is displayed")
my_dreams.click()
full_windows=driver.window_handles
assert len(full_windows)==3
for window in full_windows:
    driver.switch_to.window(window)
    print(driver.current_url)
rows=driver.find_elements("xpath","//table/tbody/tr")
row_count=len(rows)
assert row_count==10



