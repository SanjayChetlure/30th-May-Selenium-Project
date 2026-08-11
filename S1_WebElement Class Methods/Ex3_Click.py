
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

#click on male radio button
driver.find_element(By.XPATH,"//input[@id='male']").click()

#click on sunday checkbox
driver.find_element(By.XPATH,"//input[@id='sunday']").click()

time.sleep(10)


