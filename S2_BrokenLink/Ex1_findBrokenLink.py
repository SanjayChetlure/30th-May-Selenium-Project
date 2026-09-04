import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


driver = webdriver.Chrome()
driver.get("https://demoqa.com/broken")
time.sleep(5)

#1: get all links from webpage
allLinks = driver.find_elements(By.XPATH, "//a")


for link in allLinks:                       #retrieve link
   url = link.get_attribute("href")        #  get url from each link
   if url is None or url == "":
       continue
   try:
       response = requests.get(url)         # get http response of each link
       if response.status_code >= 400:      #check statusCode from response is of 200 or 400 series
           print(f"Broken link: {url} --> {response.status_code}")
       else:
           print(f"Valid link: {url}")
   except:
       print(f"Error checking: {url}")
driver.quit()
