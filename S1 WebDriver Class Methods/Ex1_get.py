import time
from selenium import webdriver


driver=webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(3)
driver.get("https://www.flipkart.com/")

time.sleep(10)