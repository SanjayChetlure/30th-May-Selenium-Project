import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
driver.find_element(By.XPATH,"//input[contains(@id,'na')]").send_keys("abc")

#Enter Email
driver.find_element(By.XPATH,"//input[contains(@placeholder,'EMail')]").send_keys("abc1234@gmail.com")

#Enter Phone num
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Phone')]").send_keys("9999999999")

#Enter Address
driver.find_element(By.XPATH,"//textarea[contains(@id,'text')]").send_keys("hffhe ajdj asodjfo lkfwqklf")

time.sleep(10)