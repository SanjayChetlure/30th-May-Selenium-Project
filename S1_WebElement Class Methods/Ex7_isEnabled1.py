
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

result=driver.find_element(By.XPATH,"//input[@id='singleFileInput']").is_enabled()
print(result)

if result:
    print("Element enabled")
else:
    print("Element disabled")

time.sleep(10)


