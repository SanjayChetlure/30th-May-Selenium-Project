print("----Ex2_Select Specific Option---")

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

#1:identify listbox
country=driver.find_element(By.XPATH,"//select[@id='country']")

#2: open listbox
country.click()
time.sleep(2)


#navigate to aus option
for i in range(5):
    country.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)


#Select Option  using Enter key
country.send_keys(Keys.ENTER)

time.sleep(10)

