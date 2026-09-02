
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Name']").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"[placeholder='Enter Name']").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"[placeholder='Enter Name'][class='form-control']").send_keys("abc")

#Enter pwd
driver.find_element(By.CSS_SELECTOR,"[id='email']").send_keys("xyz")

time.sleep(10)