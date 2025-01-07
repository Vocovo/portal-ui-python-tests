from locators import LoginPage, HomePage, ForgotPassword
from pytest import mark
from qase_client import QaseClient
import time
import os
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from conftest import qase_test


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1966")
@qase_test(case_id=1966)  # Use the decorator for Qase integration
def test_user_login(driver, run_id):
    """
    Verify that the user can log in successfully using valid credentials and access the portal.
    """

    # Initialize page objects
    login_page = LoginPage(driver=driver)
    home_page = HomePage(driver=driver)

    # STEP 1: Navigate to the production base URL
    base_url = os.getenv("PROD_UK_BASE_URL")
    driver.get(base_url)

    # STEP 2: Input valid email and password into the login fields
    login_page.input_email_field.input_text(os.getenv("ADMIN_USERNAME"))
    login_page.input_password_field.input_text(os.getenv("ADMIN_PASSWORD"))

    # STEP 3: Submit the login form
    login_page.login_button.click()

    # STEP 4: Verify that the profile avatar is displayed, indicating successful login
    assert home_page.avatar_logo_button.is_displayed(), \
        "Profile avatar not found, login may have failed."

    # STEP 5: Open the profile menu
    home_page.avatar_logo_button.click()

    # STEP 6: Verify that the profile menu item is displayed
    assert home_page.profile_menu_item.is_displayed(), \
        "Profile menu item is not displayed, indicating profile menu did not open."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1967")
@qase_test(case_id=1967)  # Use the decorator for Qase integration
def test_user_negative_login_attempt(driver, run_id):
    """
    Verify that the system displays an appropriate error message when invalid credentials are used.
    """

    # Initialize page objects
    login_page = LoginPage(driver=driver)

    # Define the expected error message
    expected_error_message = "Invalid username or password. Ensure your account is verified."

    # STEP 1: Navigate to the production base URL
    base_url = os.getenv("PROD_UK_BASE_URL")
    driver.get(base_url)

    # STEP 2: Input the user's email and an invalid password
    login_page.input_email_field.input_text(os.getenv("ADMIN_USERNAME"))
    login_page.input_password_field.input_text("wrongpasswordforsure")

    # STEP 3: Submit the login form
    login_page.login_button.click()

    # STEP 4: Verify that the error message is displayed
    assert login_page.login_error_message.is_displayed(), \
        "The error message is not displayed; login might have succeeded unexpectedly."

    # STEP 5: Verify that the displayed error message matches the expected message
    actual_error_message = login_page.login_error_message.get_text
    assert actual_error_message == expected_error_message, \
        f"Expected error message '{expected_error_message}', but got '{actual_error_message}'."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1968")
@qase_test(case_id=1968)  # Use the decorator for Qase integration
def test_user_forgot_password(driver, run_id):
    """
    Verify that the user can access the 'forgot password' page and successfully request a password reset.
    """

    # Initialize page objects
    login_page = LoginPage(driver=driver)
    forgot_password_page = ForgotPassword(driver=driver)

    # Define expected messages
    expected_forgot_password_text = "Request password reset"
    expected_success_message = "Request successful"
    expected_info_message = (
        "Request successful. You should receive an email with further instructions shortly (usually within 30 seconds)."
    )

    # STEP 1: Navigate to the production base URL
    base_url = os.getenv("PROD_UK_BASE_URL")
    driver.get(base_url)

    # STEP 2: Click the "Forgot password" link
    login_page.forgot_password_link.click()
    assert forgot_password_page.title_text.get_text == expected_forgot_password_text, \
        "Did not navigate to the 'Request password reset' page."

    # STEP 3: Enter the email address for password reset
    forgot_password_page.email_field.input_text("qa-testing@vocovo.com")

    # STEP 4: Click the "Request reset" button and verify the success message
    forgot_password_page.request_reset_button.click()
    assert forgot_password_page.request_successful_message.get_text == expected_success_message, \
        "Request successful message not displayed."

    # STEP 5: Verify the additional information message
    assert forgot_password_page.info_message.get_text == expected_info_message, \
        "Information message not displayed as expected."
