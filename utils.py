from selenium.webdriver.common.by import By


def scroll_to_element(driver_login, locator):
    if isinstance(locator, str):
        locator = (By.XPATH, locator)
    element = driver_login.find_element(*locator)
    driver_login.execute_script("arguments[0].scrollIntoView();", element)
    driver_login.execute_script("window.scrollBy(0, -90);")
