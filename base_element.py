import platform
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time
from selenium.webdriver.support.ui import Select

class BaseElement:
    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators if isinstance(locators, list) else [locators]
        self.web_element = None
        self.find()

    def find(self, retries=3, wait_time=2):
        """Finds the element with retry logic and supports fallback locators."""
        while retries > 0:
            for locator in self.locators:
                try:
                    self.web_element = WebDriverWait(self.driver, 30).until(
                        EC.visibility_of_element_located((locator.by, locator.value))
                    )
                    return self.web_element  # If found, return the element
                except TimeoutException:
                    print(f"TimeoutException: Unable to locate element with locator {locator}")
                except StaleElementReferenceException:
                    print(f"StaleElementReferenceException: Element with locator {locator} became stale.")
            retries -= 1
            time.sleep(wait_time)

        raise TimeoutException(f"None of the locators worked: {self.locators}")

    def clear(self):
        assert self.web_element
        os_name = platform.system()
        if os_name == "Darwin":  # macOS
            self.web_element.send_keys(Keys.COMMAND + "a")
        elif os_name == "Windows":  # Windows
            self.web_element.send_keys(Keys.CONTROL + "a")
        else:
            try:
                self.web_element.send_keys(Keys.CONTROL + "a")
            except:
                self.web_element.send_keys(Keys.COMMAND + "a")
        self.web_element.send_keys(Keys.BACKSPACE)
        return None

    def input_text(self, txt):
        assert self.web_element
        self.web_element.send_keys(txt)
        return None

    def click(self, retries=3, wait_time=2):
        while retries > 0:
            try:
                element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((self.locators[0].by, self.locators[0].value)))
                element.click()
                return None
            except (StaleElementReferenceException, TimeoutException):
                retries -= 1
                if retries == 0:
                    raise Exception(f"Element with locators {self.locators} could not be clicked after retries.")
                time.sleep(wait_time)

    def is_selected(self):
        return self.web_element.is_selected()

    def send_keys(self, keys):
        assert self.web_element
        self.web_element.send_keys(keys)
        return None

    def perform_action(self, *actions):
        assert self.web_element
        action_chains = ActionChains(self.driver)
        for action in actions:
            action_chains = action_chains.add_action(action)
        action_chains.perform()
        return None

    @property
    def get_text(self):
        assert self.web_element
        retries = 3
        while retries > 0:
            try:
                if self.web_element.tag_name in ["input", "textarea"]:
                    return self.web_element.get_attribute("value")
                else:
                    return self.web_element.text
            except (StaleElementReferenceException, TimeoutException):
                retries -= 1
                time.sleep(2)
        raise Exception(f"Could not get text from element {self.locators} after retries.")

    def is_displayed(self):
        return self.web_element.is_displayed()

    def is_enabled(self):
        return self.web_element.is_enabled()

    def get_selected_option_text(self):
        select_element = Select(self.web_element)
        return select_element.first_selected_option.text

    def get_attribute(self, attribute_name):
        """Returns the value of the specified attribute."""
        assert self.web_element
        return self.web_element.get_attribute(attribute_name)

    def wait_for_value(self, threshold=0, timeout=10):
        """
        Wait for the value of the element to be greater than the given threshold.
        """
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                value = int(self.get_text)
                if value > threshold:
                    return value
            except (ValueError, StaleElementReferenceException, TimeoutException):
                pass
            time.sleep(0.5)
