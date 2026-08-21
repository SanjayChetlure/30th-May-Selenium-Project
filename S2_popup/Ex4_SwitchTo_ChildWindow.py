import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://skpatro.github.io/demo/links/")

#click NewTab link from main page
driver.find_element(By.XPATH,"//input[@name='NewTab']").click()
time.sleep(5)


#get child window id
ids=driver.window_handles      #[addressOfMainPage, addressOfChildWindow]           #returns address of mainPage & childWindow

mainPageId=ids[0]
childWindowId=ids[1]

#switch to child window
driver.switch_to.window(childWindowId)      #String ChildWindowId

#click on Training link from child window popup
driver.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()
time.sleep(20)

