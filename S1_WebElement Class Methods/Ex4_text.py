
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#get text of header element
actHeaderText=driver.find_element(By.XPATH,"//h1[@class='title']").text
print(actHeaderText)

print("---")

print(driver.find_element(By.XPATH,"//h1[@class='title']").text)

time.sleep(10)

