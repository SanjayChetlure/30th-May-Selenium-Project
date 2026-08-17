
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

colour=driver.find_element(By.XPATH,"//select[@id='colors']")
s=Select(colour)

s.select_by_index(2)
s.select_by_index(0)
s.select_by_index(1)



# actText=s.first_selected_option.text
# print(actText)

print(s.first_selected_option.text)




time.sleep(10)

