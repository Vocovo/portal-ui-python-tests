from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    input_email_field = (By.ID, "email")
    input_password_field = (By.ID, "password")
    login_button = (By.XPATH, "//button[span[text()='Log in']]")


class HomePage(BasePage):
    avatar_logo_button = (By.XPATH, "//span[@data-test='vocovo-avatar']//span[text()='QTV']")
    profile_menu_item = (By.XPATH, "//a[text()='Profile']")
