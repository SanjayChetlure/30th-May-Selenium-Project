
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#click on playwright practice link
driver.find_element(By.XPATH,"//a[contains(text(),'Playwright')]").click()


time.sleep(10)