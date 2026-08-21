
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://autotestsandbox.com/examples/nested-iframes")

#Switch to outer frame
driver.switch_to.frame(0)

#get text from outer from element
outerText=driver.find_element(By.XPATH,"//p[text()='Outer iframe']").text
print(outerText)

#switch to inner frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Inner']"))

#get text from inner frame element
InnerText=driver.find_element(By.XPATH,"//p[text()='Inner iframe content']").text
print(InnerText)

time.sleep(10)

