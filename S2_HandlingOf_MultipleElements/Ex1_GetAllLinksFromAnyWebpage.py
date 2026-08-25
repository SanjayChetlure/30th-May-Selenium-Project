
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

allLinks=driver.find_elements(By.XPATH,"//a")

for singleLink in allLinks:
    print(singleLink.text)

print(len(allLinks))

