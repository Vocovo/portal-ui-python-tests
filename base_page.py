from selenium.webdriver.common.by import By
from locator import Locator
from base_element import BaseElement

class BasePage:
    def __init_subclass__(cls) -> None:
        for key, value in cls.__dict__.items():
            if key.startswith("_"):
                continue
            if callable(value):
                continue
            if key in BasePage.__dict__:
                continue
            if not isinstance(value, (str, tuple, list)):
                continue
            if isinstance(value, str):
                value = [(By.XPATH, value)]
            elif isinstance(value, tuple):
                value = [value]

            @property
            def accessor(self, value=value):
                locators = [Locator(*v) for v in value]
                return BaseElement(driver=self.driver, locators=locators)

            setattr(cls, key, accessor)

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)