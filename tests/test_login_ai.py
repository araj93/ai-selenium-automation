from core.driver_factory import get_driver
from pages.login_page import LoginPage

def test_login_ai():
    driver = get_driver()
    driver.get("https://example.com/login")

    page = LoginPage(driver)
    page.login("admin", "password")

    driver.quit()
