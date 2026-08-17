
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

country=driver.find_element(By.XPATH,"//select[@id='country']")
s=Select(country)

# s1=s.first_selected_option
# actText=s1.text
# print(actText)

# s1=s.first_selected_option
# print(s1.text)

actText=s.first_selected_option.text
print(actText)

print(s.first_selected_option.text)




time.sleep(10)

