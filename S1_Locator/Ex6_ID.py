import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
driver.find_element(By.ID,"name").send_keys("abc")

#Enter Email
driver.find_element(By.ID,"email").send_keys("abc1234@gmail.com")


time.sleep(10)
