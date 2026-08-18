
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://autotestsandbox.com/examples/nested-iframes")

# Switch to Frame
# driver.switch_to.frame("")      #String name/Id
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Outer nested frame']"))    #frame webelement
driver.switch_to.frame(0)

outerText=driver.find_element(By.XPATH,"//p[text()='Outer iframe']").text
print(outerText)


time.sleep(10)

