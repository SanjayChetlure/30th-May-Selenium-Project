print("----Ex1_Perform Action On Customized Listbox---")

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

#1:
country=driver.find_element(By.XPATH,"//select[@id='country']")

#2:
country.click()
time.sleep(2)

#3: perform keyboard action
#arrow down
country.send_keys(Keys.ARROW_DOWN)
time.sleep(2)

# arrow up
country.send_keys(Keys.ARROW_UP)
time.sleep(2)

#Select Option
country.send_keys(Keys.ENTER)

time.sleep(10)

