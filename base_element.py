import platform
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.support.ui import Select


class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def clear(self):
        assert self.web_element
        # Detect the operating system
        os_name = platform.system()
        if os_name == "Darwin":  # macOS
            self.web_element.send_keys(Keys.COMMAND + "a")
        elif os_name == "Windows":  # Windows
            self.web_element.send_keys(Keys.CONTROL + "a")
        else:  # Try both as a fallback
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
                element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.locator))
                element.click()
                return None
            except StaleElementReferenceException:
                retries -= 1
                time.sleep(wait_time)
                # Wait for the element to be present again before retrying
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.locator))
        raise StaleElementReferenceException("Element not found even after retries.")

    def is_selected(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return element.is_selected()

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
        # Check if the element is an input or textarea and get its value
        if self.web_element.tag_name in ["input", "textarea"]:
            return self.web_element.get_attribute("value")
        else:
            return self.web_element.text

    def is_displayed(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.locator))
        self.web_element = element
        return element.is_displayed()

    def is_enabled(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.locator))
        self.web_element = element
        return element.is_enabled()

    def get_selected_option_text(self):
        select_element = Select(self.web_element)
        selected_option = select_element.first_selected_option
        return selected_option.text

    def get_attribute(self, attribute_name):
        """Returns the value of the specified attribute."""
        assert self.web_element
        return self.web_element.get_attribute(attribute_name)
