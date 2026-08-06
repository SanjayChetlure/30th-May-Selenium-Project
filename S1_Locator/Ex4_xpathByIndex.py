import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
driver.find_element(By.XPATH,"(//input[@class='form-control'])[1]").send_keys("abc")

#Enter Email
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("abc1234@gmail.com")

# Enter Phone
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("9999999999")
time.sleep(10)