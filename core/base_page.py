from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ai.locator_healer import heal_locator

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, by, locator):
        try:
            return self.driver.find_element(by, locator)
        except NoSuchElementException:
            print(" Locator failed, invoking AI...")
            healed = heal_locator(locator, self.driver.page_source)
            print(f" AI suggested locator: {healed}")
            return self.driver.find_element(By.XPATH, healed)
