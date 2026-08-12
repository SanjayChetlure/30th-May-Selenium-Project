
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//input[@id='sunday']").click()
time.sleep(2)

result=driver.find_element(By.XPATH,"//input[@id='sunday']").is_selected()
print(result)

if result:
    print("checkbox is selected")
else:
    print("checkbox is De-Selected")

time.sleep(10)


