

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Login import SwagLabLoginPage


driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)

login=SwagLabLoginPage(driver)
login.enterUN()
login.enterPWD()
login.clickOnLoginBtn()



time.sleep(5)