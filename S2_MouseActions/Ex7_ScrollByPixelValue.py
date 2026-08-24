import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

act=ActionChains(driver)

#scroll down 1st para=0, 2nd para=+ve values
act.scroll_by_amount(0,700).perform()
time.sleep(5)

#scroll down 1st para=0, 2nd para=-ve values
act.scroll_by_amount(0,-300).perform()
time.sleep(5)


# #scroll right 1st para=+ve, 2nd para=0 values
# act.scroll_by_amount(100,0).perform()
# time.sleep(5)
#
# #scroll left 1st para=-ve, 2nd para=0 values
# act.scroll_by_amount(-100,0).perform()
# time.sleep(5)

# for i in range(20):
#     act.scroll_by_amount(0, 100).perform()
#     time.sleep(0.5)

time.sleep(50)

