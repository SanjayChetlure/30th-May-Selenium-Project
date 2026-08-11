
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
#Apr1
# driver.find_element(By.XPATH,"//input[@id='name']").send_keys("abc")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@id='name']").clear()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@id='name']").send_keys("xyz")


#Apr2
s1=driver.find_element(By.XPATH,"//input[@id='name']")
s1.send_keys("abc")
time.sleep(2)
s1.clear()
time.sleep(2)
s1.send_keys("xyz")


time.sleep(10)


