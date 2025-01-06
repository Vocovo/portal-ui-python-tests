from locators import (HomePageControllers, HomePageHeadsetsModal, HeadsetsDetailsPage, HomePageHandsetsModal,
                      HandsetsDetailsPage, HomePageCallPointsModal, HomePageKeyPadsModal, CallPointsDetailsPage,
                      KeypadsDetailsPage, HomePage)
from pytest import mark
from qase_client import QaseClient
import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1965")
def test_filtering_by_group_internal_vocovo(driver_uk_prod_login_admin, run_id):
    """Verify that filtering works by selecting a group (Vocovo Internal)"""

    homepage = HomePage(driver_uk_prod_login_admin)
    hpc = HomePageControllers(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("CE-1965".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Get the base filter title from the homepage
        # EXPECTED RESULT: The filter should be set to "Strongbyte Solutions Ltd"
        base_filter_title = homepage.dropdown_button.get_text
        assert base_filter_title == "Strongbyte Solutions Ltd", (
            f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
        )

        # STEP 2: Retrieve the number of active devices from the default dashboard -> headsets
        # EXPECTED RESULT: The number should reflect the correct count of active devices.
        default_page_headsets_active_number = hpc.active_devices_count.get_text

        # STEP 3: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 4: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 5: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 6: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # STEP 7: Retrieve the number of active devices from the Vocovo Internal Group dashboard -> headsets
        # EXPECTED RESULT: The number should reflect the correct count of active devices according to the filters.
        vocovo_internal_active_number = hpc.active_devices_count.get_text

        # STEP 8: Verify that the number of active devices changes according to the filters
        # EXPECTED RESULT: The number should reflect the correct number of active devices according to the filters
        assert default_page_headsets_active_number != vocovo_internal_active_number

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion or Selenium exception, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1977")
def test_filtering_by_group_internal_vocovo_active_controllers(driver_uk_prod_login_admin, run_id):
    """After filtering by selecting a group the "Active" controllers belonging
    to that group are being shown on the dashboard"""

    homepage = HomePage(driver_uk_prod_login_admin)
    hpc = HomePageControllers(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("CE-1977".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Get the base filter title from the homepage
        # EXPECTED RESULT: The filter should be set to "Strongbyte Solutions Ltd"
        base_filter_title = homepage.dropdown_button.get_text
        assert base_filter_title == "Strongbyte Solutions Ltd", (
            f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
        )

        # STEP 2: Retrieve the number of active devices from the default dashboard -> headsets
        # EXPECTED RESULT: The number should reflect the correct count of active devices.
        default_page_headsets_active_number = hpc.active_devices_count.get_text

        # STEP 3: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 4: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 5: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 6: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # STEP 7: Retrieve the number of active devices from the Vocovo Internal Group dashboard -> headsets
        # EXPECTED RESULT: The number should reflect the correct count of active devices according to the filters.
        vocovo_internal_active_number = hpc.active_devices_count.get_text

        # STEP 8: Verify that the number of active devices changes according to the filters
        # EXPECTED RESULT: The number should reflect the correct number of active devices according to the filters
        assert default_page_headsets_active_number != vocovo_internal_active_number

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion or Selenium exception, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1978")
def test_filtering_by_group_internal_vocovo_inactive_controllers(driver_uk_prod_login_admin, run_id):
    """After filtering by selecting a group the "Inactive"
    controllers belonging to that group are being shown on the dashboard"""

    homepage = HomePage(driver_uk_prod_login_admin)
    hpc = HomePageControllers(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("CE-1978".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Get the base filter title from the homepage
        # EXPECTED RESULT: The filter should be set to "Strongbyte Solutions Ltd"
        base_filter_title = homepage.dropdown_button.get_text
        assert base_filter_title == "Strongbyte Solutions Ltd", (
            f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
        )

        # STEP 2: Retrieve the number of inactive devices from the default dashboard -> headsets
        # EXPECTED RESULT: The number should reflect the correct count of inactive devices.
        default_page_headsets_inactive_number = hpc.inactive_devices_count.get_text

        # STEP 3: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 4: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 5: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 6: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # STEP 7: Retrieve the number of inactive devices from the Vocovo Internal Group dashboard -> headsets
        # EXPECTED RESULT: The number should reflect the correct count of inactive devices according to the filters.
        vocovo_internal_inactive_number = hpc.inactive_devices_count.get_text

        # STEP 8: Verify that the number of inactive devices changes according to the filters
        # EXPECTED RESULT: The number should reflect the correct number of inactive devices according to the filters
        assert default_page_headsets_inactive_number != vocovo_internal_inactive_number

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion or Selenium exception, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1979")
def test_filtering_by_group_internal_vocovo_fault_controllers(driver_uk_prod_login_admin, run_id):
    """After filtering by selecting a group the "Fault" controllers belonging
    to that group are being shown on the dashboard"""

    homepage = HomePage(driver_uk_prod_login_admin)
    hpc = HomePageControllers(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("CE-1979".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Get the base filter title from the homepage
        # EXPECTED RESULT: The filter should be set to "Strongbyte Solutions Ltd"
        base_filter_title = homepage.dropdown_button.get_text
        assert base_filter_title == "Strongbyte Solutions Ltd", (
            f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
        )

        # STEP 2: Get the default number of fault devices
        # EXPECTED RESULT: The default number should be the number of fault devices on the dashboard.
        default_page_headsets_fault_number = hpc.fault_devices_title.get_text

        # STEP 3: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 4: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 5: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 6: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # STEP 7: Verify that the number of fault devices changes according to the filters
        # EXPECTED RESULT: The number should reflect the correct number of fault devices according to the filters
        vocovo_internal_fault_number = hpc.fault_devices_count.get_text
        assert default_page_headsets_fault_number != vocovo_internal_fault_number, (
            f"Expected fault devices count to change, but it remained {default_page_headsets_fault_number}"
        )

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion or Selenium exception, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise
    
    
@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1980")
def test_filtering_by_group_internal_vocovo_unknown_status_controllers(driver_uk_prod_login_admin, run_id):
    """After filtering by selecting a group the "Unknown status" controllers are being displayed on the dashboard"""

    homepage = HomePage(driver_uk_prod_login_admin)
    hpc = HomePageControllers(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("CE-1980".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Get the base filter title from the homepage
        # EXPECTED RESULT: The filter should be set to "Strongbyte Solutions Ltd"
        base_filter_title = homepage.dropdown_button.get_text
        assert base_filter_title == "Strongbyte Solutions Ltd", (
            f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
        )

        # STEP 2: Retrieve the number of "Unknown status" devices from the default dashboard -> headsets
        # EXPECTED RESULT: The number should reflect the correct count of "Unknown status" devices.
        default_page_headsets_unknown_status_number = hpc.unknown_status_devices_count.get_text

        # STEP 3: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 4: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 5: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 6: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # STEP 7: Retrieve the number of "Unknown status" devices from the Vocovo Internal Group dashboard -> headsets
        # EXPECTED RESULT: The number should reflect the correct count of "Unknown status" devices according to the filters.
        vocovo_internal_unknown_number = hpc.unknown_status_devices_count.get_text

        # STEP 8: Verify that the number of "Unknown status" devices changes according to the filters
        # EXPECTED RESULT: The number should reflect the correct number of "Unknown status" devices according to the filters
        assert default_page_headsets_unknown_status_number != vocovo_internal_unknown_number

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion or Selenium exception, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1981")
def test_filtering_by_group_internal_vocovo_headset_modal(driver_uk_prod_login_admin, run_id):
    """Verify that the headsets module displays all necessary data for the
    selected group (online, offline, offline for more than 30 days, and unknown)"""

    homepage = HomePage(driver_uk_prod_login_admin)
    hpc = HomePageControllers(driver_uk_prod_login_admin)
    hphm = HomePageHeadsetsModal(driver_uk_prod_login_admin)
    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("CE-1981".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Get the base filter title from the homepage
        # EXPECTED RESULT: The filter should be set to "Strongbyte Solutions Ltd"
        base_filter_title = homepage.dropdown_button.get_text
        assert base_filter_title == "Strongbyte Solutions Ltd", (
            f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
        )

        # STEP 2: Retrieve the values from the Strongbyte Solutions Ltd Group dashboard -> headsets
        # EXPECTED RESULT: The number should reflect the correct number of headsets for each status.
        default_page_online_headsets = hphm.online_count.get_text
        default_page_offline_headsets = hphm.offline_count.get_text
        default_page_offline_30_days = hphm.long_offline_count.get_text
        default_page_unknown_headsets = hphm.unknown_count.get_text

        # STEP 3: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 4: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 5: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 6: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # STEP 7: Retrieve the values from the Vocovo Internal Group dashboard -> headsets
        # EXPECTED RESULT: The number should reflect the correct number of headsets for each status.
        vocovo_internal_page_online_headsets = hphm.online_count.get_text
        vocovo_internal_page_offline_headsets = hphm.offline_count.get_text
        vocovo_internal_page_offline_30_days = hphm.long_offline_count.get_text
        vocovo_internal_page_unknown_headsets = hphm.unknown_count.get_text

        # STEP 8: Verify that the number of headsets changes according to the filters
        # EXPECTED RESULT: The number should reflect the correct number of headsets according to the filters
        assert default_page_online_headsets != vocovo_internal_page_online_headsets
        assert default_page_offline_headsets != vocovo_internal_page_offline_headsets
        assert default_page_offline_30_days != vocovo_internal_page_offline_30_days
        assert default_page_unknown_headsets != vocovo_internal_page_unknown_headsets

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion or Selenium exception, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1982")
def test_navigate_to_the_headsets_module_details_page_for_a_group(driver_uk_prod_login_admin, run_id):
    """Verify that clicking on the headsets module will redirect the user to the headsets details page for that group"""

    # Record the start time before the test begins
    start_time = time.time()

    homepage = HomePage(driver_uk_prod_login_admin)
    hphm = HomePageHeadsetsModal(driver_uk_prod_login_admin)
    headset_details = HeadsetsDetailsPage(driver_uk_prod_login_admin)

    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Retrieve the values from the Strongbyte Solutions Ltd Group dashboard -> headsets
    default_page_online_headsets = hphm.online_count.get_text
    default_page_offline_headsets = hphm.offline_count.get_text
    default_page_offline_30_days = hphm.long_offline_count.get_text
    default_page_unknown_headsets = hphm.unknown_count.get_text

    case_id = int("CE-1982".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 2: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 3: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 4: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # Retrieve the values from the Vocovo Internal Group dashboard -> headsets
        vocovo_internal_page_online_headsets = hphm.online_count.get_text
        vocovo_internal_page_offline_headsets = hphm.offline_count.get_text
        vocovo_internal_page_offline_30_days = hphm.long_offline_count.get_text
        vocovo_internal_page_unknown_headsets = hphm.unknown_count.get_text

        # More checks to make sure that the group has indeed been changed
        assert default_page_online_headsets != vocovo_internal_page_online_headsets
        assert default_page_offline_headsets != vocovo_internal_page_offline_headsets
        assert default_page_offline_30_days != vocovo_internal_page_offline_30_days
        assert default_page_unknown_headsets != vocovo_internal_page_unknown_headsets

        # STEP 5: Click on the headsets modal under the Vocovo Internal group
        # EXPECTED RESULT: The user should be directed to the details page of the headsets for that group
        hphm.headsets_modal_title.click()

        assert "Headsets" in headset_details.headsets_details_page_title.get_text

        if vocovo_internal_page_online_headsets == "-":
            vocovo_internal_page_online_headsets = "0"
        if vocovo_internal_page_offline_headsets == "-":
            vocovo_internal_page_offline_headsets = "0"
        if vocovo_internal_page_offline_30_days == "-":
            vocovo_internal_page_offline_30_days = "0"
        if vocovo_internal_page_unknown_headsets == "-":
            vocovo_internal_page_unknown_headsets = "0"

        # Checks to make sure that the headsets details page indeed belongs to the VoCoVo Internal Group
        time.sleep(3)
        online_headsets = headset_details.online_count.get_text
        offline_headsets = headset_details.offline_count.get_text
        offline_for_more = headset_details.long_offline_count.get_text
        unknown_headsets = headset_details.unknown_count.get_text

        assert vocovo_internal_page_online_headsets == online_headsets
        assert vocovo_internal_page_offline_headsets == offline_headsets
        assert vocovo_internal_page_offline_30_days == offline_for_more
        assert vocovo_internal_page_unknown_headsets == unknown_headsets

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1983")
@mark.workingon
def test_filtering_by_group_internal_vocovo_handsets_modal(driver_uk_prod_login_admin, run_id):
    """Verify that the handsets module displays all necessary data for the selected group
    (online, offline, offline for more than 30 days, and unknown)"""

    homepage = HomePage(driver_uk_prod_login_admin)
    handsets = HomePageHandsetsModal(driver_uk_prod_login_admin)

    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("CE-1983".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Get the base filter title from the homepage
        # EXPECTED RESULT: The filter should be set to "Strongbyte Solutions Ltd"
        base_filter_title = homepage.dropdown_button.get_text
        assert base_filter_title == "Strongbyte Solutions Ltd", (
            f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
        )

        # STEP 2: Retrieve the values from the Strongbyte Solutions Ltd Group dashboard -> handsets
        # EXPECTED RESULT: The number of devices should be the correct count for each category.
        default_page_online_handsets = handsets.online_count.get_text
        default_page_offline_handsets = handsets.offline_count.get_text
        default_page_offline_30_days = handsets.long_offline_count.get_text
        default_page_unknown_handsets = handsets.unknown_count.get_text

        # STEP 3: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 4: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 5: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 6: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # STEP 7: Retrieve the values from the Vocovo Internal Group dashboard -> handsets
        # EXPECTED RESULT: The number of devices should be the correct count for each category.
        vocovo_internal_page_online_handsets = handsets.online_count.get_text
        vocovo_internal_page_offline_handsets = handsets.offline_count.get_text
        vocovo_internal_page_offline_30_days = handsets.long_offline_count.get_text
        vocovo_internal_page_unknown_handsets = handsets.unknown_count.get_text

        # STEP 8: Verify that the number of handsets changes according to the filters
        # EXPECTED RESULT: The number should reflect the correct number of handsets according to the filters
        assert default_page_online_handsets != vocovo_internal_page_online_handsets
        assert default_page_offline_handsets != vocovo_internal_page_offline_handsets
        assert default_page_offline_30_days != vocovo_internal_page_offline_30_days
        assert default_page_unknown_handsets != vocovo_internal_page_unknown_handsets

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1984")
def test_navigate_to_the_handsets_module_details_page_for_a_group(driver_uk_prod_login_admin, run_id):
    """Verify that clicking on the handsets module will redirect the user to the handsets details page for that group"""

    # Record the start time before the test begins
    start_time = time.time()

    homepage = HomePage(driver_uk_prod_login_admin)
    handsetshomepage = HomePageHandsetsModal(driver_uk_prod_login_admin)
    handset_details = HandsetsDetailsPage(driver_uk_prod_login_admin)

    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Retrieve the values from the Strongbyte Solutions Ltd Group dashboard -> handsets
    default_page_online_handsets = handsetshomepage.online_count.get_text
    default_page_offline_handsets = handsetshomepage.offline_count.get_text
    default_page_offline_30_days = handsetshomepage.long_offline_count.get_text
    default_page_unknown_handsets = handsetshomepage.unknown_count.get_text

    case_id = int("CE-1984".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 2: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 3: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 4: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # Retrieve the values from the Vocovo Internal Group dashboard -> handsets
        vocovo_internal_page_online_handsets = handsetshomepage.online_count.get_text
        vocovo_internal_page_offline_handsets = handsetshomepage.offline_count.get_text
        vocovo_internal_page_offline_30_days = handsetshomepage.long_offline_count.get_text
        vocovo_internal_page_unknown_handsets = handsetshomepage.unknown_count.get_text

        # Handle edge cases where the count might be "-"
        if vocovo_internal_page_online_handsets == "-":
            vocovo_internal_page_online_handsets = "0"
        if vocovo_internal_page_offline_handsets == "-":
            vocovo_internal_page_offline_handsets = "0"
        if vocovo_internal_page_offline_30_days == "-":
            vocovo_internal_page_offline_30_days = "0"
        if vocovo_internal_page_unknown_handsets == "-":
            vocovo_internal_page_unknown_handsets = "0"

        # More checks to make sure that the group has indeed been changed
        assert default_page_online_handsets != vocovo_internal_page_online_handsets
        assert default_page_offline_handsets != vocovo_internal_page_offline_handsets
        assert default_page_offline_30_days != vocovo_internal_page_offline_30_days
        assert default_page_unknown_handsets != vocovo_internal_page_unknown_handsets

        # STEP 5: Click on the handsets modal under the Vocovo Internal group
        # EXPECTED RESULT: The user should be directed to the details page of the headsets for that group
        handsetshomepage.handsets_modal_title.click()

        assert "Handsets" in handset_details.handsets_details_page_title.get_text

        # Checks to make sure that the handsets details page indeed belongs to the VoCoVo Internal Group
        time.sleep(3)
        online_handsets = handset_details.online_count.get_text
        offline_handsets = handset_details.offline_count.get_text
        offline_for_more = handset_details.long_offline_count.get_text
        unknown_handsets = handset_details.unknown_count.get_text

        assert vocovo_internal_page_online_handsets == online_handsets
        assert vocovo_internal_page_offline_handsets == offline_handsets
        assert vocovo_internal_page_offline_30_days == offline_for_more
        assert vocovo_internal_page_unknown_handsets == unknown_handsets

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1985")
def test_filtering_by_group_internal_vocovo_callpoints_modal(driver_uk_prod_login_admin, run_id):
    """Verify that the call points module displays all necessary data for the
    selected group (online, offline, offline for more than 30 days, and unknown)"""

    homepage = HomePage(driver_uk_prod_login_admin)
    callpoints = HomePageCallPointsModal(driver_uk_prod_login_admin)

    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("CE-1985".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Get the base filter title from the homepage
        # EXPECTED RESULT: The filter should be set to "Strongbyte Solutions Ltd"
        base_filter_title = homepage.dropdown_button.get_text
        assert base_filter_title == "Strongbyte Solutions Ltd", (
            f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
        )

        # STEP 2: Retrieve the values from the Strongbyte Solutions Ltd Group dashboard -> call points
        # EXPECTED RESULT: The number of devices should be the correct count for each category.
        default_page_online_callpoints = callpoints.online_count.get_text
        default_page_offline_callpoints = callpoints.offline_count.get_text
        default_page_offline_30_days = callpoints.long_offline_count.get_text
        default_page_unknown_callpoints = callpoints.unknown_count.get_text

        # STEP 3: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 4: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 5: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 6: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # Retrieve the values from the Vocovo Internal Group dashboard -> call points
        vocovo_internal_page_online_callpoints = callpoints.online_count.get_text
        vocovo_internal_page_offline_callpoints = callpoints.offline_count.get_text
        vocovo_internal_page_offline_30_days = callpoints.long_offline_count.get_text
        vocovo_internal_page_unknown_callpoints = callpoints.unknown_count.get_text

        # Handle edge cases where the count might be "-"
        if vocovo_internal_page_online_callpoints == "-":
            vocovo_internal_page_online_callpoints = "0"

        if vocovo_internal_page_offline_callpoints == "-":
            vocovo_internal_page_offline_callpoints = "0"

        if vocovo_internal_page_offline_30_days == "-":
            vocovo_internal_page_offline_30_days = "0"

        if vocovo_internal_page_unknown_callpoints == "-":
            vocovo_internal_page_unknown_callpoints = "0"

        # STEP 7: Verify that the number of active devices changes according to the filters
        # EXPECTED RESULT: The number should reflect the correct number of active devices according to the filters
        assert default_page_online_callpoints != vocovo_internal_page_online_callpoints
        assert default_page_offline_callpoints != vocovo_internal_page_offline_callpoints
        assert default_page_offline_30_days != vocovo_internal_page_offline_30_days
        assert default_page_unknown_callpoints != vocovo_internal_page_unknown_callpoints

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1986")
def test_navigate_to_the_callpoints_module_details_page_for_a_group(driver_uk_prod_login_admin, run_id):
    """Verify that clicking on the call points module will redirect
    the user to the headsets details page for that group"""
    # Record the start time before the test begins
    start_time = time.time()

    homepage = HomePage(driver_uk_prod_login_admin)
    callpoointshome = HomePageCallPointsModal(driver_uk_prod_login_admin)
    callpoints_details = CallPointsDetailsPage(driver_uk_prod_login_admin)

    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Retrieve the values from the Strongbyte Solutions Ltd Group dashboard -> callpoints
    default_page_online_callpoints = callpoointshome.online_count.get_text
    default_page_offline_callpoints = callpoointshome.offline_count.get_text
    default_page_offline_30_days = callpoointshome.long_offline_count.get_text
    default_page_unknown_callpoints = callpoointshome.unknown_count.get_text

    case_id = int("CE-1986".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 2: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 3: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 4: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # Retrieve the values from the Vocovo Internal Group dashboard -> call points
        vocovo_internal_page_online_callpoints = callpoointshome.online_count.get_text
        vocovo_internal_page_offline_callpoints = callpoointshome.offline_count.get_text
        vocovo_internal_page_offline_30_days = callpoointshome.long_offline_count.get_text
        vocovo_internal_page_unknown_callpoints = callpoointshome.unknown_count.get_text

        # Handle edge cases where the count might be "-"
        if vocovo_internal_page_online_callpoints == "-":
            vocovo_internal_page_online_callpoints = "0"

        if vocovo_internal_page_offline_callpoints == "-":
            vocovo_internal_page_offline_callpoints = "0"

        if vocovo_internal_page_offline_30_days == "-":
            vocovo_internal_page_offline_30_days = "0"

        if vocovo_internal_page_unknown_callpoints == "-":
            vocovo_internal_page_unknown_callpoints = "0"

        # STEP 5: Verify that the number of active devices changes according to the filters
        # EXPECTED RESULT: The number should reflect the correct number of active devices according to the filters
        assert default_page_online_callpoints != vocovo_internal_page_online_callpoints
        assert default_page_offline_callpoints != vocovo_internal_page_offline_callpoints
        assert default_page_offline_30_days != vocovo_internal_page_offline_30_days
        assert default_page_unknown_callpoints != vocovo_internal_page_unknown_callpoints

        # STEP 6: Click on the callpoints modal under the Vocovo Internal group
        # EXPECTED RESULT: The user should be directed to the details page of the call points for that group
        callpoointshome.callpoints_modal_title.click()

        assert "Call Points" in callpoints_details.callpoints_details_page_title.get_text

        # Checks to make sure that the call points details page indeed belongs to the VoCoVo Internal Group
        time.sleep(3)
        online_callpoints = callpoints_details.online_count.get_text
        offline_callpoints = callpoints_details.offline_count.get_text
        offline_for_more = callpoints_details.long_offline_count.get_text
        unknown_callpoints = callpoints_details.unknown_count.get_text

        assert vocovo_internal_page_online_callpoints == online_callpoints
        assert vocovo_internal_page_offline_callpoints == offline_callpoints
        assert vocovo_internal_page_offline_30_days == offline_for_more
        assert vocovo_internal_page_unknown_callpoints == unknown_callpoints

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1987")
def test_filtering_by_group_internal_vocovo_keypads_modal(driver_uk_prod_login_admin, run_id):
    """Verify that the keypads module displays all necessary data for the
    selected group (online, offline, offline for more than 30 days, and unknown)"""

    homepage = HomePage(driver_uk_prod_login_admin)
    keypads = HomePageKeyPadsModal(driver_uk_prod_login_admin)

    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    base_filter_title = homepage.dropdown_button.get_text

    # On the homepage dashboard the filter should be set to "Strongbyte Solutions Ltd"
    assert base_filter_title == "Strongbyte Solutions Ltd"

    # Retrieve the values from the Strongbyte Solutions Ltd Group dashboard -> keypads
    default_page_online_keypads = keypads.online_count.get_text
    default_page_offline_keypads = keypads.offline_count.get_text
    default_page_offline_30_days = keypads.long_offline_count.get_text
    default_page_unknown_keypads = keypads.unknown_count.get_text

    # Record the start time before the test begins
    start_time = time.time()

    case_id = int("CE-1987".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 2: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 3: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 4: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # Retrieve the values from the Vocovo Internal Group dashboard -> keypads
        vocovo_internal_page_online_keypads = keypads.online_count.get_text
        vocovo_internal_page_offline_keypads = keypads.offline_count.get_text
        vocovo_internal_page_offline_30_days = keypads.long_offline_count.get_text
        vocovo_internal_page_unknown_keypads = keypads.unknown_count.get_text

        # Handle edge cases where the count might be "-"
        if vocovo_internal_page_online_keypads == "-":
            vocovo_internal_page_online_keypads = "0"

        if vocovo_internal_page_offline_keypads == "-":
            vocovo_internal_page_offline_keypads = "0"

        if vocovo_internal_page_offline_30_days == "-":
            vocovo_internal_page_offline_30_days = "0"

        if vocovo_internal_page_unknown_keypads == "-":
            vocovo_internal_page_unknown_keypads = "0"

        # STEP 5: Verify that the number of keypads changes according to the filters
        # EXPECTED RESULT: The number should reflect the correct number of keypads according to the filters
        assert default_page_online_keypads != vocovo_internal_page_online_keypads
        assert default_page_offline_keypads != vocovo_internal_page_offline_keypads
        assert default_page_offline_30_days != vocovo_internal_page_offline_30_days
        assert default_page_unknown_keypads != vocovo_internal_page_unknown_keypads

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1988")
def test_navigate_to_the_keypads_module_details_page_for_a_group(driver_uk_prod_login_admin, run_id):
    """Verify that clicking on the keypads module will redirect the user to the headsets details page for that group"""
    # Record the start time before the test begins
    start_time = time.time()

    homepage = HomePage(driver_uk_prod_login_admin)
    keypadshome = HomePageKeyPadsModal(driver_uk_prod_login_admin)
    keypads_details = KeypadsDetailsPage(driver_uk_prod_login_admin)

    failure_reason = None  # Initialize failure_reason to None
    qase_client = QaseClient()  # Initialize the Qase client

    # Retrieve the values from the Strongbyte Solutions Ltd Group dashboard -> keypads
    default_page_online_keypads = keypadshome.online_count.get_text
    default_page_offline_keypads = keypadshome.offline_count.get_text
    default_page_offline_30_days = keypadshome.long_offline_count.get_text
    default_page_unknown_keypads = keypadshome.unknown_count.get_text

    case_id = int("CE-1988".split('-')[1])

    # Initialize elapsed_time with a default value
    elapsed_time = None

    try:
        # STEP 1: Click the dropdown button
        # EXPECTED RESULT: The dropdown menu should open.
        homepage.dropdown_button.click()

        # STEP 2: Type "Vocovo Internal" into the input field
        # EXPECTED RESULT: The input field should accept the text.
        homepage.dropdown_input.send_keys("Vocovo Internal")

        # STEP 3: Click on the "Vocovo Internal" option from the dropdown list
        # EXPECTED RESULT: The dropdown should close, and the selection should be made.
        homepage.dropdown_vocovo_internal_option.click()

        # STEP 4: Verify that the "VoCoVo Internal" label is displayed
        # EXPECTED RESULT: The label should contain the text "VoCoVo Internal".
        assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
            "The filtering label does not match the expected text."

        # Retrieve the values from the Vocovo Internal Group dashboard -> keypads
        vocovo_internal_page_online_keypads = keypadshome.online_count.get_text
        vocovo_internal_page_offline_keypads = keypadshome.offline_count.get_text
        vocovo_internal_page_offline_30_days = keypadshome.long_offline_count.get_text
        vocovo_internal_page_unknown_keypads = keypadshome.unknown_count.get_text

        # Handle edge cases where the count might be "-"
        if vocovo_internal_page_online_keypads == "-":
            vocovo_internal_page_online_keypads = "0"

        if vocovo_internal_page_offline_keypads == "-":
            vocovo_internal_page_offline_keypads = "0"

        if vocovo_internal_page_offline_30_days == "-":
            vocovo_internal_page_offline_30_days = "0"

        if vocovo_internal_page_unknown_keypads == "-":
            vocovo_internal_page_unknown_keypads = "0"

        # STEP 5: Verify that the number of keypads changes according to the filters
        # EXPECTED RESULT: The number should reflect the correct number of keypads according to the filters
        assert default_page_online_keypads != vocovo_internal_page_online_keypads
        assert default_page_offline_keypads != vocovo_internal_page_offline_keypads
        assert default_page_offline_30_days != vocovo_internal_page_offline_30_days
        assert default_page_unknown_keypads != vocovo_internal_page_unknown_keypads

        # STEP 6: Click on the keypads modal under the Vocovo Internal group
        # EXPECTED RESULT: The user should be directed to the details page of the keypads for that group
        keypadshome.keypads_modal_title.click()

        assert "Keypads" in keypads_details.keypads_details_page_title.get_text

        # Checks to make sure that the keypads details page indeed belongs to the VoCoVo Internal Group
        time.sleep(3)
        online_keypads = keypads_details.online_count.get_text
        offline_keypads = keypads_details.offline_count.get_text
        offline_for_more = keypads_details.long_offline_count.get_text
        unknown_keypads = keypads_details.unknown_count.get_text

        assert vocovo_internal_page_online_keypads == online_keypads
        assert vocovo_internal_page_offline_keypads == offline_keypads
        assert vocovo_internal_page_offline_30_days == offline_for_more
        assert vocovo_internal_page_unknown_keypads == unknown_keypads

        # Record the end time after the test completes
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "passed", comment="Test completed successfully",
                                       time=int(elapsed_time))  # Use the elapsed time here

    except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
        # If there's an assertion error, capture the failure reason
        failure_reason = str(e)
        # Record the end time after the test completes (in case of failure)
        end_time = time.time()
        # Calculate the time taken for the test to run in seconds
        elapsed_time = end_time - start_time

        # Pass the elapsed time (in seconds) to the Qase update_test_result method
        qase_client.update_test_result(run_id, case_id, "failed", comment=f"Test failed. Reason: {failure_reason}",
                                       time=int(elapsed_time))  # Use the elapsed time here

        # Re-raise the exception to ensure the test is marked as failed
        raise