import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.mobikwik.com/")

time.sleep(2)

#click on login btn
driver.find_element(By.XPATH,"(//span[text()='Login'])[1]").click()
time.sleep(2)

#Enter mobile num
driver.find_element(By.XPATH,"//input[@name='userId']").send_keys("999999999")
time.sleep(20)