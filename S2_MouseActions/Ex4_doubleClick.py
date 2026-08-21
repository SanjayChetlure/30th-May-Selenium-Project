

import time
from importlib.util import source_hash

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(5)


element=driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")
act=ActionChains(driver)

#Apr1:
# act.move_to_element(element).perform()
# act.double_click().perform()
print("----")

#Apr2:
# act.move_to_element(element).double_click().perform()

#Apr3:
act.double_click(element).perform()




time.sleep(50)
