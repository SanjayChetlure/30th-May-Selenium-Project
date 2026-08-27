
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)

#click on close btn
driver.find_element(By.XPATH,"//span[@class='b3wTlE']").click()
time.sleep(3)

#search mobile
driver.find_element(By.XPATH,"(//input[@class='nw1UBF v1zwn25'])[1]").send_keys("redmi note 15 5g")
time.sleep(1)

#click on search icon
driver.find_element(By.XPATH,"(//button[@class='XFwMiH'])[1]").click()

#get ratings
ratings=driver.find_element(By.XPATH,"((//div[@class='jIjQ8S'])[1]//span)[6]").text
print(ratings)

#get reviews
reviews=driver.find_element(By.XPATH,"((//div[@class='jIjQ8S'])[1]//span)[8]").text
print(reviews)


time.sleep(20)


