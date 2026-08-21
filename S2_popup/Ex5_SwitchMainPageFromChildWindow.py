import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://skpatro.github.io/demo/links/")

# click NewTab link from main page
driver.find_element(By.XPATH, "//input[@name='NewTab']").click()
time.sleep(5)

# get child window id
ids = driver.window_handles  # [addressOfMainPage, addressOfChildWindow]           #returns address of mainPage & childWindow

# switch to child window
driver.switch_to.window(ids[1])  # String ChildWindowId

# click on Training link from child window popup
driver.find_element(By.XPATH, "(//span[text()='Training'])[1]").click()
time.sleep(5)


# switch to main page from child window
driver.switch_to.window(ids[0])            # String mainPageId
time.sleep(2)

# click NewWindow link from main page
driver.find_element(By.XPATH, "//input[@name='NewWindow']").click()
time.sleep(5)

latestIds=driver.window_handles    # [addressOfMainPage, addressOfChildWindow1, addressOfChildWindo2]

#switch to child window2
driver.switch_to.window(latestIds[2])
time.sleep(2)
driver.close()

time.sleep(20)

