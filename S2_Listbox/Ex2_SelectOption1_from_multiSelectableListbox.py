
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#1: identify listbox
colour=driver.find_element(By.XPATH,"//select[@id='colors']")

#2: Create object of Select class
s=Select(colour)

#3: call select class methods to select options from listbox
s.select_by_visible_text("Green")
s.select_by_visible_text("Blue")

time.sleep(10)

