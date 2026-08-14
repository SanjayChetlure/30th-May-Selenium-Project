
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#1: identify listbox
country=driver.find_element(By.XPATH,"//select[@id='country']")

#2: Create object of Select class
s=Select(country)

#3: call select class methods to select options from listbox
# s.select_by_visible_text("India")       #String text
# s.select_by_value("uk")          #String value
s.select_by_index(9)                #int index


time.sleep(10)

