
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
time.sleep(3)

#click on close btn
driver.find_element(By.XPATH,"//span[@class='b3wTlE']").click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,"input.nw1UBF.v1zwn26").send_keys("abc")


time.sleep(10)