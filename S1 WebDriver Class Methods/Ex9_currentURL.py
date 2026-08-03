import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://www.google.com/")

actURL=driver.current_url
print(actURL)


time.sleep(10)