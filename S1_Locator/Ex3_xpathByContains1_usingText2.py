
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#click on Simple Alert link
driver.find_element(By.XPATH,"//button[contains(text(),'Simple')]").click()


time.sleep(10)