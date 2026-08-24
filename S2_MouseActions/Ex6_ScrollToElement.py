

import time
from importlib.util import source_hash

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)


section3=driver.find_element(By.XPATH,"//h4[text()='Section 3']")
act=ActionChains(driver)

act.scroll_to_element(section3).perform()

time.sleep(50)
