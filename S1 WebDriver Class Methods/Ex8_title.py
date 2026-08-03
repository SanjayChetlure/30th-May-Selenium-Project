import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://www.google.com/")

expTitle="Google"
actTitle=driver.title
print(actTitle)

if actTitle==expTitle:
    print("Pass")
else:
    print("Fail")

print("-----")

print(driver.title)

time.sleep(10)