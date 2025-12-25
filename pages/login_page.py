from selenium.webdriver.common.by import By
from core.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = "//input[@id='username']"
    PASSWORD = "//input[@id='password']"
    LOGIN_BTN = "//button[@type='submit']"

    def login(self, user, pwd):
        self.find(By.XPATH, self.USERNAME).send_keys(user)
        self.find(By.XPATH, self.PASSWORD).send_keys(pwd)
        self.find(By.XPATH, self.LOGIN_BTN).click()
