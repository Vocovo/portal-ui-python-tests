from locators import (HomePageControllers, HomePageHeadsetsModal, HeadsetsDetailsPage, HomePageHandsetsModal,
                      HandsetsDetailsPage, HomePageCallPointsModal, HomePageKeyPadsModal, CallPointsDetailsPage,
                      KeypadsDetailsPage)
from pytest import mark
from qase_client import QaseClient
import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import traceback


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-1")
def test_dashboard_active_devices(driver_uk_prod_login_admin, run_id):
    """Verify that "Active" controllers are being shown on the dashboard"""

    hce = HomePageControllers(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-1".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Load the production base URL from environment variables
        # EXPECTED RESULT: The system should load the login page at the specified base URL.
        active_controllers = hce.active_devices_title.get_text
        assert active_controllers == "Active", "The title for active devices does not match 'Active'"

        # STEP 2: Retrieve the count of active controllers
        active_controllers_count = int(hce.active_devices_count.get_text)
        assert active_controllers_count > 0, "The count of active devices should be greater than 0."
        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time
        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time
        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-2")
def test_dashboard_inactive_devices(driver_uk_prod_login_admin, run_id):
    """Verify that "Inactive" controllers are being shown on the dashboard"""

    hce = HomePageControllers(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-2".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Load the production base URL from environment variables
        # EXPECTED RESULT: The system should load the login page at the specified base URL.
        # (This step is implicitly handled by the `driver_uk_prod_login_admin` fixture)

        # STEP 2: Retrieve the "Inactive Devices" title text from the dashboard
        # EXPECTED RESULT: The text should match "Inactive".
        inactive_controllers_title = hce.inactive_devices_title.get_text
        assert inactive_controllers_title == "Inactive", (
            f"Expected 'Inactive', but got '{inactive_controllers_title}'"
        )

        # STEP 3: Retrieve the count of inactive devices from the dashboard
        # EXPECTED RESULT: The count should be greater than zero.
        inactive_controllers_count = int(hce.inactive_devices_count.get_text)
        assert inactive_controllers_count > 0, (
            f"Expected inactive devices count to be greater than 0, but got {inactive_controllers_count}"
        )

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-3")
def test_dashboard_fault_devices(driver_uk_prod_login_admin, run_id):
    """Verify that "Fault" controllers are being displayed on the dashboard"""

    hce = HomePageControllers(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-3".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Load the production base URL from environment variables
        # EXPECTED RESULT: The system should load the login page at the specified base URL.
        # (This step is implicitly handled by the `driver_uk_prod_login_admin` fixture)

        # STEP 2: Retrieve the "Fault" title text from the dashboard
        # EXPECTED RESULT: The text should match "Fault".
        fault_devices_title = hce.fault_devices_title.get_text
        assert fault_devices_title == "Fault", (
            f"Expected 'Fault', but got '{fault_devices_title}'"
        )

        # STEP 3: Retrieve the count of fault devices from the dashboard
        # EXPECTED RESULT: The count should be greater than zero.
        fault_devices_count = int(hce.fault_devices_count.get_text)
        assert fault_devices_count > 0, (
            f"Expected fault devices count to be greater than 0, but got {fault_devices_count}"
        )

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-4")
def test_dashboard_unknown_status(driver_uk_prod_login_admin, run_id):
    """Verify that "Unknown status" controllers are being displayed on the dashboard"""

    # TEST CASE ID = 279452
    hce = HomePageControllers(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-4".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Load the production base URL from environment variables
        # EXPECTED RESULT: The system should load the login page at the specified base URL.
        # (Handled by the driver fixture)

        # STEP 2: Retrieve the text for the "Unknown status" label
        # EXPECTED RESULT: The label "Unknown status" should be displayed on the dashboard.
        unknown_status_label = hce.unknown_status_devices_title.get_text
        assert unknown_status_label == "Unknown status", (
            "The label for 'Unknown status' is incorrect or not displayed."
        )

        # STEP 3: Retrieve the count of devices with "Unknown status"
        # EXPECTED RESULT: The count should be a positive integer greater than 0.
        unknown_status_count = int(hce.unknown_status_devices_count.get_text)
        assert unknown_status_count > 0, (
            f"The count of 'Unknown status' devices is {unknown_status_count}, which is not greater than 0."
        )

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-5")
def test_dashboard_active_controllers(driver_uk_prod_login_admin, run_id):
    """Verify that the "Active" controllers number is higher than 10K"""

    # TEST CASE ID = 279453
    hce = HomePageControllers(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-5".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Load the production base URL from environment variables
        # EXPECTED RESULT: The system should load the login page at the specified base URL.
        # (Handled by the driver fixture)

        # STEP 2: Retrieve the "Active" controllers title text from the dashboard
        # EXPECTED RESULT: The text should match "Active".
        active_controllers_title = hce.active_devices_title.get_text
        assert active_controllers_title == "Active", (
            f"Expected 'Active', but got '{active_controllers_title}'"
        )

        # STEP 3: Retrieve the count of active controllers from the dashboard
        # EXPECTED RESULT: The count should be greater than 10,000.
        active_controllers_count = int(hce.active_devices_count.get_text)
        assert active_controllers_count > 10000, (
            f"Expected active controllers count to be greater than 10,000, but got {active_controllers_count}"
        )

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # Capture the failure reason and traceback
        failure_reason = str(e)
        stacktrace = traceback.format_exc()

        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method with the failure reason and stack trace
        qase_client.update_test_result(run_id, case_id, "failed",
                                       comment=f"Test failed. Reason: {failure_reason}\nStacktrace:\n{stacktrace}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


# HOMEPAGE DASHBOARD -> DEVICES -> HEADSETS
@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-10")
def test_dashboard_headsets(driver_uk_prod_login_admin, run_id):
    """Verify that the headsets module displays all necessary data
    (online, offline, offline for more than 30 days, and unknown)."""

    hm = HomePageHeadsetsModal(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Define the expected labels and add descriptive error messages for each assertion
    labels_and_counts = {
        "online": ("Online", hm.online_label, hm.online_count),
        "offline": ("Offline", hm.offline_label, hm.offline_count),
        "long offline": ("Offline for more than 30 days", hm.long_offline_label, hm.long_offline_count),
        "unknown": ("Unknown", hm.unknown_label, hm.unknown_count)
    }

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-10".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Load the production base URL from environment variables
        # EXPECTED RESULT: The system should load the login page at the specified base URL.
        # (This step is implicitly handled by the `driver_uk_prod_login_admin` fixture)

        # Verify each label and count dynamically
        for label_name, (expected_text, label_element, count_element) in labels_and_counts.items():
            # STEP 2: Verify that the label is displayed with the correct text
            # EXPECTED RESULT: The label should match the expected text.
            assert label_element.get_text == expected_text, (
                f"Expected '{expected_text}' label for {label_name} but got '{label_element.get_text}'"
            )

            # STEP 3: Verify that the count is greater than zero
            # EXPECTED RESULT: The count should be a positive integer.
            assert int(count_element.get_text) > 0, (
                f"Expected {label_name} count to be greater than 0, but got {count_element.get_text}"
            )

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-11")
def test_navigate_to_headsets_details_page_from_dashboard(driver_uk_prod_login_admin, run_id):
    """Verify that the user is able to click on the "Headsets" section,
    and they get redirected to the Headsets details page."""

    hm = HomePageHeadsetsModal(driver_uk_prod_login_admin)
    hd = HeadsetsDetailsPage(driver_uk_prod_login_admin)

    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-11".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Click on the "Headsets" section in the modal.
        # EXPECTED RESULT: The system should navigate to the Headsets details page.
        hm.headsets_modal_title.click()

        # STEP 2: Verify that the Headsets details page title is displayed.
        # EXPECTED RESULT: The Headsets details page title element should be visible.
        assert hd.headsets_details_page_title.is_displayed()

        # STEP 3: Verify that the Headsets details page title contains the word "Headset".
        # EXPECTED RESULT: The text of the Headsets details page title should include "Headset".
        assert "Headset" in hd.headsets_details_page_title.get_text, "The title does not contain 'Headset'"

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


# HOMEPAGE DASHBOARD -> DEVICES -> HANDSETS
@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-12")
def test_dashboard_handsets(driver_uk_prod_login_admin, run_id):
    """Verify that the handsets module displays all necessary data
    (online, offline, offline for more than 30 days, and unknown)."""

    hndset = HomePageHandsetsModal(driver_uk_prod_login_admin)

    # Initialize failure_reason to None and Qase client
    failure_reason = None
    qase_client = QaseClient()

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-12".split('-')[1])  # Extract case ID from marker

    # Initialize elapsed_time with a default value
    elapsed_time = None

    labels_and_counts = {
        "online": ("Online", hndset.online_label, hndset.online_count),
        "offline": ("Offline", hndset.offline_label, hndset.offline_count),
        "long offline": ("Offline for more than 30 days", hndset.long_offline_label, hndset.long_offline_count),
        "unknown": ("Unknown", hndset.unknown_label, hndset.unknown_count)
    }

    try:
        # STEP 1: Verify that the label is displayed with the correct text for each status type.
        # EXPECTED RESULT: The label should match the expected text (e.g., "Online", "Offline").
        for label_name, (expected_text, label_element, count_element) in labels_and_counts.items():
            assert label_element.get_text == expected_text, (
                f"Expected '{expected_text}' label for {label_name} but got '{label_element.get_text}'"
            )

            # STEP 2: Verify that the count is greater than zero for each status type.
            # EXPECTED RESULT: The count should be a positive integer, indicating items are present for each status.
            assert int(count_element.get_text) > 0, (
                f"Expected {label_name} count to be greater than 0, but got {count_element.get_text}"
            )

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-13")
def test_navigate_to_handsets_details_page_from_dashboard(driver_uk_prod_login_admin, run_id):
    """Verify that the user is able to click on the "Headsets" section,
    and they get redirected to the Handsets details page."""

    hm = HomePageHandsetsModal(driver_uk_prod_login_admin)
    hd = HandsetsDetailsPage(driver_uk_prod_login_admin)

    # Initialize failure_reason to None and Qase client
    failure_reason = None
    qase_client = QaseClient()

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-13".split('-')[1])  # Extract case ID from marker

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Click on the "Handsets" section in the modal.
        # EXPECTED RESULT: The system should navigate to the Handsets details page.
        hm.handsets_modal_title.click()

        # STEP 2: Verify that the Handsets details page title is displayed.
        # EXPECTED RESULT: The Handsets page title element should be visible.
        assert hd.handsets_details_page_title.is_displayed()

        # STEP 3: Verify that the Handsets page title contains the word "Handset".
        # EXPECTED RESULT: The text of the Handsets page title should include "Handset".
        assert "Handset" in hd.handsets_details_page_title.get_text, ("Expected to navigate to the handsets "
                                                              "details page, navigated somewhere else instead")

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


# HOMEPAGE DASHBOARD -> DEVICES -> CALL POINTS
@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-14")
def test_dashboard_callpoints(driver_uk_prod_login_admin, run_id):
    """Verify that the call points module displays all necessary data
    (online, offline, offline for more than 30 days, and unknown)."""

    callpoints = HomePageCallPointsModal(driver_uk_prod_login_admin)

    # Initialize failure_reason to None and Qase client
    failure_reason = None
    qase_client = QaseClient()

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-14".split('-')[1])  # Extract case ID from marker

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        labels_and_counts = {
            "online": ("Online", callpoints.online_label, callpoints.online_count),
            "offline": ("Offline", callpoints.offline_label, callpoints.offline_count),
            "long offline": ("Offline for more than 30 days", callpoints.long_offline_label, callpoints.long_offline_count),
            "unknown": ("Unknown", callpoints.unknown_label, callpoints.unknown_count)
        }

        for label_name, (expected_text, label_element, count_element) in labels_and_counts.items():
            # STEP 1: Verify that the label is displayed with the correct text for each status type.
            # EXPECTED RESULT: The label should match the expected text (e.g., "Online", "Offline").
            assert label_element.get_text == expected_text, (
                f"Expected '{expected_text}' label for {label_name} but got '{label_element.get_text}'"
            )

            # STEP 2: Verify that the count is greater than zero for each status type.
            # EXPECTED RESULT: The count should be a positive integer, indicating items are present for each status.
            assert int(count_element.get_text) > 0, (
                f"Expected {label_name} count to be greater than 0, but got {count_element.get_text}"
            )

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-15")
def test_navigate_to_callpoints_details_page_from_dashboard(driver_uk_prod_login_admin, run_id):
    """Verify that the user is able to click on the "Call Points" section,
    and they get redirected to the Call Points details page."""

    cp = HomePageCallPointsModal(driver_uk_prod_login_admin)
    cd = CallPointsDetailsPage(driver_uk_prod_login_admin)

    # Initialize failure_reason to None and Qase client
    failure_reason = None
    qase_client = QaseClient()

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-15".split('-')[1])  # Extract case ID from marker

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Click on the "Call Points" section in the modal.
        # EXPECTED RESULT: The system should navigate to the Call Points details page.
        cp.callpoints_modal_title.click()

        # STEP 2: Verify that the Call Points details page title is displayed.
        # EXPECTED RESULT: The Call Points page title element should be visible.
        assert cd.callpoints_details_page_title.is_displayed()

        # STEP 3: Verify that the Call Points page title contains the word "Call Points".
        # EXPECTED RESULT: The text of the Call Points page title should include "Call Points".
        assert "Call Points" in cd.callpoints_details_page_title.get_text, (
            "Expected to navigate to the call points details page, navigated somewhere else instead"
        )

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


# HOMEPAGE DASHBOARD -> DEVICES -> KEYPADS
@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("PST-16")
def test_dashboard_keypads(driver_uk_prod_login_admin, run_id):
    """Verify that the keypads module displays all necessary data
    (online, offline, offline for more than 30 days, and unknown)."""

    keypads = HomePageKeyPadsModal(driver_uk_prod_login_admin)
    qase_client = QaseClient()  # Initialize the Qase client

    labels_and_counts = {
        "online": ("Online", keypads.online_label, keypads.online_count),
        "offline": ("Offline", keypads.offline_label, keypads.offline_count),
        "long offline": ("Offline for more than 30 days", keypads.long_offline_label, keypads.long_offline_count),
        "unknown": ("Unknown", keypads.unknown_label, keypads.unknown_count)
    }

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-16".split('-')[1])  # Extract case ID from marker

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Navigate to the dashboard and login (handled by fixture)
        # EXPECTED RESULT: The system should load the login page and navigate to the dashboard.

        # STEP 2: Verify that the label is displayed with the correct text for each status type.
        # EXPECTED RESULT: The label should match the expected text (e.g., "Online", "Offline").
        for label_name, (expected_text, label_element, count_element) in labels_and_counts.items():
            assert label_element.get_text == expected_text, (
                f"Expected '{expected_text}' label for {label_name} but got '{label_element.get_text}'"
            )

            # STEP 3: Verify that the count is greater than zero for each status type.
            # EXPECTED RESULT: The count should be a positive integer, indicating items are present for each status.
            assert int(count_element.get_text) > 0, (
                f"Expected {label_name} count to be greater than 0, but got {count_element.get_text}"
            )

        # Record the end time after the test completes
        end_time = time.time()

        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
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
@mark.testcaseid("PST-17")
def test_navigate_to_keypads_details_page_from_dashboard(driver_uk_prod_login_admin, run_id):
    """Verify that the user is able to click on the "Keypads"
    section, and they get redirected to the Keypads details page"""

    hmkp = HomePageKeyPadsModal(driver_uk_prod_login_admin)
    kp = KeypadsDetailsPage(driver_uk_prod_login_admin)

    # Initialize failure_reason to None and Qase client
    failure_reason = None
    qase_client = QaseClient()

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("PST-17".split('-')[1])  # Extract case ID from marker

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Navigate to the dashboard and login (handled by fixture)
        # EXPECTED RESULT: The system should be on the dashboard page, and the user should be logged in.

        # STEP 2: Click on the "Keypads" section in the modal.
        # EXPECTED RESULT: The system should navigate to the Keypads details page.
        hmkp.keypads_modal_title.click()

        # STEP 3: Verify that the Keypads details page title is displayed.
        # EXPECTED RESULT: The Keypads page title element should be visible.
        assert kp.keypads_details_page_title.is_displayed()

        # STEP 4: Verify that the Keypads page title contains the word "Keypads".
        # EXPECTED RESULT: The text of the Keypads page title should include "Keypads".
        assert "Keypads" in kp.keypads_details_page_title.get_text, (
            "Expected to navigate to the keypads details page, navigated somewhere else instead"
        )

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise
