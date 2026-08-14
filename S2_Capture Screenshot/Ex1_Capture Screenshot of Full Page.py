
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

driver.save_screenshot("D:\\Python\\Batches\\30th May 2026 Python Automation\\Screenshots\\abc1.png")




time.sleep(10)

