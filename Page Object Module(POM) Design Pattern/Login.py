#POM class 1
from selenium.webdriver.common.by import By


class SwagLabLoginPage:

    #1: declare webelements xpath as class variable
    username="(//input[@class='input_error form_input'])[1]"
    password="//input[@name='password']"
    login="//input[@name='login-button']"


    #2: Initialize driver within Constructor
    def __init__(self,driver):
        self.driver=driver


    #3: perform action on webelements within method
    def enterUN(self):
        self.driver.find_element(By.XPATH,self.username).send_keys("standard_user")

    def enterPWD(self):
        self.driver.find_element(By.XPATH, self.password).send_keys("secret_sauce")

    def clickOnLoginBtn(self):
        self.driver.find_element(By.XPATH,self.login).click()


