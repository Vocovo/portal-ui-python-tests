from base_element import BaseElement
from selenium.webdriver.common.by import By
from locator import Locator


class BasePage:

    def __init_subclass__(cls) -> None:
        for key, value in cls.__dict__.items():
            if key.startswith("_"):
                continue
            if callable(value):
                continue
            if key in BasePage.__dict__:
                continue
            if not isinstance(value, (str, tuple)):
                continue
            if isinstance(value, str):
                value = (By.XPATH, value)

            @property
            def accessor(self, value=value):
                locator = Locator(*value)
                return BaseElement(driver=self.driver, locator=locator)

            setattr(cls, key, accessor)

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
