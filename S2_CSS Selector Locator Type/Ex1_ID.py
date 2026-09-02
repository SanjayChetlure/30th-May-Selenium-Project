
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
# driver.find_element(By.CSS_SELECTOR,"input#name").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"*#name").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("abc")

#Enter pwd
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("xyz")

time.sleep(10)