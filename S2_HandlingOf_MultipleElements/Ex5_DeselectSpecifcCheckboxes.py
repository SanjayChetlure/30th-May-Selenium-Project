import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:/D:/Python/Workspace/30th%20May%20Selenium%20Project/Html%20File/MultipleCheckboxes.html")

allCheckboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for singleCheckbox in allCheckboxes:
    singleCheckbox.click()
    time.sleep(0.5)


count=1
for singleCheckbox in allCheckboxes:
    if count!=5 and count!=8:
        singleCheckbox.click()
        time.sleep(0.5)
    count+=1
time.sleep(50)

