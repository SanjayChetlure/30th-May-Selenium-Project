
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

colour=driver.find_element(By.XPATH,"//select[@id='colors']")
s=Select(colour)

allOptions=s.options

for eachOption in allOptions:
    print(eachOption.text)


time.sleep(10)

