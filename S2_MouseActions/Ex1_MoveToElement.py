
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

# 1: Identify mouse over element
login=driver.find_element(By.XPATH,"//span[text()='Login']")

# 2: Create an object ActionChain class with driver object as input
act=ActionChains(driver)

# 3: Call method - move_to_element() to display options from mouse over, which accept webElement obj as a input
act.move_to_element(login).perform()
time.sleep(5)

#click on orders link
driver.find_element(By.XPATH,"//div[text()='Orders']").click()

time.sleep(50)
