
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
# driver.find_element(By.CSS_SELECTOR,"input#name").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,"input#name").send_keys("abc")

time.sleep(10)