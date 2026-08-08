import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#click on Home link
driver.find_element(By.LINK_TEXT,"Blog").click()

time.sleep(20)
