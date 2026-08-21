
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/delete_customer.php")

time.sleep(2)

#Enter customer id
driver.find_element(By.XPATH,"//input[@name='cusid']").send_keys("123")

#click on submit btn
driver.find_element(By.XPATH,"//input[@name='submit']").click()


#Switch to alert popup
alt=driver.switch_to.alert           #returns Alert class object

#1: getText from alert popup
actText=alt.text
print(actText)

# #2: click on cancel btn
# alt.dismiss()

#3: click on OK btn from 1st alert popup
alt.accept()

#4: click on OK btn from 2nd alert popup
alt.accept()




time.sleep(20)