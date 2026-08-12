
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

result=False

try:
    result = driver.find_element(By.XPATH, "(//a[text()='Home'])[1]").is_displayed()
except:
    print("Exception handled")

print(result)

if result:
    print("Element present")
else:
    print("Element not present")



time.sleep(10)


