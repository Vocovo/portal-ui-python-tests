from locators import LoginPage
from locators import HomePage
from pytest import mark
import os


@mark.smoke
def test_super_user_successful_login(driver):
    """
    Test case for superuser successful login.
    This test verifies that the superuser is able to log in
    """

    # Load the production base URL from environment variables
    base_url = os.getenv("PROD_BASE_URL")

    # Navigate to the login page
    driver.get(base_url)

    # Initialize page objects for the login and home pages
    login_page = LoginPage(driver=driver)
    home_page = HomePage(driver=driver)

    # Input the superuser's email from environment variables into the email field
    login_page.input_email_field.input_text(os.getenv("ADMIN_USERNAME"))

    # Input the superuser's password from environment variables into the password field
    login_page.input_password_field.input_text(os.getenv("ADMIN_PASSWORD"))

    # Click the login button to submit the login form
    login_page.login_button.click()

    # After logging in, verify that the profile avatar (or another identifying element) is displayed
    # This indicates that the user has logged in successfully and is on the home page
    assert home_page.avatar_logo_button.is_displayed(), "Profile avatar not found, login may have failed"

    # Click on the avatar logo to open the profile menu
    home_page.avatar_logo_button.click()

    # Verify that the profile menu item is displayed
    # This ensures that the user can access the profile options after logging in
    assert home_page.profile_menu_item.is_displayed(), "Profile menu item is not displayed"
