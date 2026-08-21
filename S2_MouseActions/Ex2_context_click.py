

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.in/")
time.sleep(5)

#click on close btn
driver.find_element(By.XPATH,"//span[@class='b3wTlE']").click()
time.sleep(3)


Cart=driver.find_element(By.XPATH,"//span[text()='Cart']")
act=ActionChains(driver)

#Apr1:
# act.move_to_element(Cart).perform()
# act.context_click().perform()

#Apr2:
# act.move_to_element(Cart).context_click().perform()

#Apr3:
act.context_click(Cart).perform()




time.sleep(50)
