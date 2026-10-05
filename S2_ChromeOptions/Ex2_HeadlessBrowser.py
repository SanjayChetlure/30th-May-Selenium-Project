import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

ops = Options()
ops.add_argument("--headless")
driver = webdriver.Chrome(options=ops)
driver.get("https://www.google.com/")
print(driver.title)
time.sleep(5)
