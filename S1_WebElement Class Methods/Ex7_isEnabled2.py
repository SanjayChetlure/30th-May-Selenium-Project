
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.testmuai.com/login/")
time.sleep(4)

result=driver.find_element(By.XPATH,"//button[text()='Continue']").is_enabled()
print(result)

if result:
    print("Element enabled")
else:
    print("Element disabled")

time.sleep(10)


