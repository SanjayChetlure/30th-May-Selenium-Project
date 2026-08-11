
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
#Apr1
# driver.find_element(By.XPATH,"//input[@id='name']").send_keys("abc")

print("----")

#Apr2
s1=driver.find_element(By.XPATH,"//input[@id='name']")
s1.send_keys("abc")

time.sleep(10)

