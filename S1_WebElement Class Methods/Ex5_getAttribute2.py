
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")


#Enter Name
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("abcd")
time.sleep(2)

#get text from input field
text=driver.find_element(By.XPATH,"//input[@id='name']").get_attribute("value")
print(text)

time.sleep(10)

