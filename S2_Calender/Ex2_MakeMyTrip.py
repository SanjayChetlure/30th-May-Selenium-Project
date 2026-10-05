from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
time.sleep(9)

# close login popup (important step)
driver.find_element(By.XPATH, "//span[@class='commonModal__close']").click()
time.sleep(3)


# click on departure field
driver.find_element(By.XPATH, "//label[@for='departure']").click()
time.sleep(3)


target_month = "January 2027"
target_day = "15"


# loop until desired month appears
while True:
   currentMonth = driver.find_element(By.XPATH, "(//div[@class='DayPicker-Caption'])[1]").text


   if target_month == currentMonth:
       break
   else:
       driver.find_element(By.XPATH, "//span[@aria-label='Next Month']").click()
   time.sleep(1)


# select date
time.sleep(3)
allDates = driver.find_elements(By.XPATH, "//div[@class='dateInnerCell']//p[1]")


for date in allDates:
   if date.text == target_day:
       date.click()
       break
   time.sleep(0.2)

# or Alternative way to select date using runtime xpath

#select target date using runtime xpath
# driver.find_element(By.XPATH, f"(//div[@class='dateInnerCell']//p[text()='{target_day}'])[1]").click()


time.sleep(10)
driver.quit()
