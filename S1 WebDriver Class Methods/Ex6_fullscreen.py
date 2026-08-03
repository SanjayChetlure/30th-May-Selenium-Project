import time
from selenium import webdriver


driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.google.com/")
time.sleep(2)
driver.fullscreen_window()


time.sleep(10)