
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

allSeletedOptions=s.all_selected_options

for i in allSeletedOptions:
   print(i.text)


# print("----")
# count=1
# for i in allSeletedOptions:
#     if count==3:
#         print(i.text)
#     count+=1






time.sleep(10)

