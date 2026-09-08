from selenium.webdriver.common.by import By


class SwagLabOpenMenuPage:

    logout="//a[text()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnLogoutBtn(self):
        self.driver.find_element(By.XPATH,self.logout).click()