from core.driver_factory import get_driver

def test_google():
    driver = get_driver()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
