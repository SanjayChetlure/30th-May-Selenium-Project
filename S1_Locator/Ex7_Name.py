import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

#Enter Name
driver.find_element(By.NAME,"email").send_keys("amol")




time.sleep(10)
