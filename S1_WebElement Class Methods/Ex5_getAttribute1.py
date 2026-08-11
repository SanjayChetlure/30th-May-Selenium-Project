
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#get text from input field
text=driver.find_element(By.XPATH,"//input[@id='name']").get_attribute("placeholder")
print(text)

time.sleep(10)

