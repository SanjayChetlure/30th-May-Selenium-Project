
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://autotestsandbox.com/examples/nested-iframes")

#Switch to outer frame
driver.switch_to.frame(0)

#Switch to inner frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Inner']"))

InnerText=driver.find_element(By.XPATH,"//p[text()='Inner iframe content']").text
print(InnerText)


#switch to main page from iframe
# driver.switch_to.default_content()

driver.switch_to.parent_frame()
driver.switch_to.parent_frame()

#perform action on main page
driver.find_element(By.XPATH,"(//a[text()='Home'])[1]").click()

time.sleep(10)

