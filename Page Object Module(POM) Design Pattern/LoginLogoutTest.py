import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Login import SwagLabLoginPage
from Home import SwagLabHomePage
from OpenMenu import SwagLabOpenMenuPage


driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)

login=SwagLabLoginPage(driver)
login.enterUN("standard_user")
time.sleep(2)
login.enterPWD("secret_sauce")
time.sleep(2)
login.clickOnLoginBtn()
time.sleep(2)

home=SwagLabHomePage(driver)
home.clickOnMenuOption()
time.sleep(2)

openMenu=SwagLabOpenMenuPage(driver)
openMenu.clickOnLogoutBtn()





time.sleep(10)




