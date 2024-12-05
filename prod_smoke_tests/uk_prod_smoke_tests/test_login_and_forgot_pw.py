from locators import LoginPage, HomePage, ForgotPassword
from pytest import mark
from qase_client import QaseClient
import time
import os


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-7")
def test_user_login(driver, run_id):
    """The user should be able to log in successfully using valid credentials and access the portal."""

    # Initialize failure_reason to None and Qase client
    failure_reason = None
    qase_client = QaseClient()

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-7".split('-')[1])  # Extract case ID from marker

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Load the production base URL from environment variables
        # EXPECTED RESULT: The system should load the login page at the specified base URL.
        base_url = os.getenv("PROD_UK_BASE_URL")
        driver.get(base_url)

        # STEP 2: Navigate to the login page
        # EXPECTED RESULT: The login page should load successfully.
        login_page = LoginPage(driver=driver)
        home_page = HomePage(driver=driver)

        # STEP 3: Input valid email and password into the login fields
        # EXPECTED RESULT: The email and password fields should accept the inputs.
        login_page.input_email_field.input_text(os.getenv("ADMIN_USERNAME"))
        login_page.input_password_field.input_text(os.getenv("ADMIN_PASSWORD"))

        # STEP 4: Click the login button to submit the login form
        # EXPECTED RESULT: The system should authenticate the user and redirect to the home page.
        login_page.login_button.click()

        # STEP 5: Verify that the profile avatar or another identifying element is displayed
        # EXPECTED RESULT: The profile avatar should be visible, indicating that the user is logged in successfully.
        assert home_page.avatar_logo_button.is_displayed(), "Profile avatar not found, login may have failed"

        # STEP 6: Click on the avatar logo to open the profile menu
        # EXPECTED RESULT: The profile menu should open, allowing access to profile options.
        home_page.avatar_logo_button.click()

        # STEP 7: Verify that the profile menu item is displayed
        # EXPECTED RESULT: The profile menu should be visible, allowing the user to access profile-related settings.
        assert home_page.profile_menu_item.is_displayed(), "Profile menu item is not displayed"

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except AssertionError as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)

        # Record the end time after the test completes (in case of failure)
        end_time = time.time()

        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method with "failed" status
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-8")
def test_user_negative_login_attempt(driver, run_id):
    """The system should display an appropriate error message when invalid credentials are used."""

    # Initialize failure_reason to None and Qase client
    failure_reason = None
    qase_client = QaseClient()

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-8".split('-')[1])  # Extract case ID from marker

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        login_failed_text = "Invalid username or password. Ensure your account is verified."

        # STEP 1: Load the production base URL from environment variables
        # EXPECTED RESULT: The system should load the login page at the specified base URL.
        base_url = os.getenv("PROD_UK_BASE_URL")

        # STEP 2: Navigate the browser to the login page using the base URL
        # EXPECTED RESULT: The login page should load successfully.
        driver.get(base_url)

        # STEP 3: Initialize the LoginPage object to interact with the login page elements
        # EXPECTED RESULT: The LoginPage object should be initialized
        # successfully, allowing interaction with the login elements.
        login_page = LoginPage(driver=driver)

        # STEP 4: Input the user's email from environment variables into the email field
        # EXPECTED RESULT: The email field should accept and display the provided email address.
        login_page.input_email_field.input_text(os.getenv("ADMIN_USERNAME"))

        # STEP 5: Input an invalid password into the password field to simulate a failed login attempt
        # EXPECTED RESULT: The password field should accept and display the provided invalid password.
        login_page.input_password_field.input_text("wrongpasswordforsure")

        # STEP 6: Click on the login button to submit the login form
        # EXPECTED RESULT: The system should attempt to authenticate the user and display an error message.
        login_page.login_button.click()

        # STEP 7: Verify that an error message is displayed after the failed login attempt
        # EXPECTED RESULT: The error message should be visible, indicating that the login attempt failed.
        assert login_page.login_error_message.is_displayed(), ("The error message is not displayed; "
                                                               "login might have succeeded unexpectedly.")

        # STEP 8: Verify that the displayed error message matches the expected message for invalid credentials
        # EXPECTED RESULT: The error message text should exactly match
        # "Invalid username or password. Ensure your account is verified."
        assert login_page.login_error_message.get_text == login_failed_text, ("The error message text does "
                                                                              "not match the expected message.")

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except AssertionError as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)

        # Record the end time after the test completes (in case of failure)
        end_time = time.time()

        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method with "failed" status
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-9")
def test_user_forgot_password(driver, run_id):
    """The user is able to access the 'forgot password' page and reset their password."""

    # Initialize failure_reason to None and Qase client
    failure_reason = None
    qase_client = QaseClient()

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-9".split('-')[1])  # Extract case ID from marker

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        forgot_password_text = "Request password reset"
        request_successful_message = "Request successful"
        info_message = ("Request successful. You should receive an email with "
                        "further instructions shortly (usually within 30 seconds).")

        # STEP 1: Load the production base URL from environment variables
        # EXPECTED RESULT: The system should load the login page at the specified base URL.
        base_url = os.getenv("PROD_UK_BASE_URL")
        driver.get(base_url)

        # STEP 2: Navigate to the login page
        # EXPECTED RESULT: The login page should load successfully.
        login_page = LoginPage(driver=driver)
        forgot_password_page = ForgotPassword(driver=driver)

        # STEP 3: Click the "forgot password" link
        # EXPECTED RESULT: The "Request password reset" page should be displayed.
        login_page.forgot_password_link.click()
        assert forgot_password_page.title_text.get_text == forgot_password_text, \
            "Did not navigate to the 'Request password reset' page."

        # STEP 4: Enter the email address for password reset
        # EXPECTED RESULT: The email input field should accept the user's email address.
        forgot_password_page.email_field.input_text("qa-testing@vocovo.com")

        # STEP 5: Click the "Request reset" button
        # EXPECTED RESULT: The system should display the "Request successful" message.
        forgot_password_page.request_reset_button.click()
        assert forgot_password_page.request_successful_message.get_text == request_successful_message, \
            "Request successful message not displayed."

        # STEP 6: Verify the success info message
        # EXPECTED RESULT: The system should display the additional
        # information message indicating that an email has been sent.
        assert forgot_password_page.info_message.get_text == info_message, "Information message not displayed as expected."

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except AssertionError as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)

        # Record the end time after the test completes (in case of failure)
        end_time = time.time()

        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method with "failed" status
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))

        # Re-raise the exception to ensure the test is marked as failed
        raise
