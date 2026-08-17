
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")


colour=driver.find_element(By.XPATH,"//select[@id='colors']")

s=Select(colour)

s.select_by_index(0)
s.select_by_index(1)
s.select_by_index(2)

time.sleep(3)

s.deselect_by_visible_text("Blue")
s.deselect_by_value("green")
s.deselect_by_index(0)

time.sleep(10)

