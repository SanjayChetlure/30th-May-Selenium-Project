import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/Python/Workspace/30th%20May%20Selenium%20Project/Html%20File/WebTable.html")
time.sleep(2)

multipleData=driver.find_elements(By.XPATH,"//table[@id='1234']//td[3]")

for i in multipleData:
    print(i.text)

time.sleep(20)


