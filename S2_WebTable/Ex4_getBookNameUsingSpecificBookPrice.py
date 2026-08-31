import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/Python/Workspace/30th%20May%20Selenium%20Project/Html%20File/WebTable.html")
time.sleep(2)

s1=driver.find_element(By.XPATH,"//table[@id='1234']//td[text()='100']//parent::tr/td[2]").text
print(s1)

time.sleep(20)


