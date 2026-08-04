
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
# driver.find_element(Locator type)
# driver.find_element(By.XPATH,"Xpath Expression")
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("abc")


#Enter Email
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abc1234@gmail.com")

#Enter Phone num
driver.find_element(By.XPATH,"//input[@placeholder='Enter Phone']").send_keys("9999999999")


#Enter Address
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("hffhe ajdj asodjfo lkfwqklf")

time.sleep(10)