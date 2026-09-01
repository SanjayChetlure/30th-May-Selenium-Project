import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/Python/Workspace/30th%20May%20Selenium%20Project/Html%20File/WebTable.html")
time.sleep(2)


allData = driver.find_elements(By.XPATH, "//table[@id='1234']//td")

emptyData = 0

for singleData in allData:
   text=singleData.text
   if text == "":
       emptyData += 1


print("Total empty fields:", emptyData)


