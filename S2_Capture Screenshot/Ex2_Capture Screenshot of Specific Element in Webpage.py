
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

# driver.find_element(By.XPATH,"//button[text()='START']").screenshot("D:\\Python\\Batches\\30th May 2026 Python Automation\\Screenshots\\start.png")

start=driver.find_element(By.XPATH,"//button[text()='START']")
start.screenshot("D:\\Python\\Batches\\30th May 2026 Python Automation\\Screenshots\\start.png")

time.sleep(10)

