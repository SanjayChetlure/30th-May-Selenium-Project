
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)

#Enter UN
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
time.sleep(2)

#Enter PWD
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
time.sleep(2)

#click on login btn
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(2)

#get Logo Text
actLogoText=driver.find_element(By.XPATH,"//div[@class='app_logo']").text
expLogoText="Swag Labs1"

if actLogoText==expLogoText:
    print("Test Case Pass")
else:
    print("Test Case Fail")


#click on menu option
driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
time.sleep(2)


#click on logout option
driver.find_element(By.XPATH,"//a[text()='Logout']").click()
time.sleep(2)



time.sleep(10)

