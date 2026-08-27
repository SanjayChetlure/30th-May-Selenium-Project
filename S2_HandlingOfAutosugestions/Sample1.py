
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

driver.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("redmi")
time.sleep(5)

allOptionsAddress=driver.find_elements(By.XPATH,"(//ul[@class='G43f7e'])[1]/li")

for eachAddres in allOptionsAddress:
    print(eachAddres.text)

expText="redmi 15"
for eachAddress in allOptionsAddress:
    actText=eachAddress.text
    if actText.__eq__(expText):
        eachAddress.click()
        break

time.sleep(50)


