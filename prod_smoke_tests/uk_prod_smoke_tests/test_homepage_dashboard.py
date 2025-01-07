from locators import (HomePageControllers, HomePageHeadsetsModal, HeadsetsDetailsPage, HomePageHandsetsModal,
                      HandsetsDetailsPage, HomePageCallPointsModal, HomePageKeyPadsModal, CallPointsDetailsPage,
                      KeypadsDetailsPage)
from pytest import mark
from qase_client import QaseClient
import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import traceback
from conftest import sanitize_count
from conftest import qase_test


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1960")
@mark.workingon
@qase_test(case_id=1960)  # Use the decorator for Qase integration
def test_dashboard_active_devices(driver_uk_prod_login_admin, run_id):
    """
    Verify that "Active" controllers are being shown on the dashboard.
    """

    # Initialize page objects
    hce = HomePageControllers(driver_uk_prod_login_admin)

    # STEP 1: Verify the title for active devices
    active_controllers_title = hce.active_devices_title.get_text
    assert active_controllers_title == "Active", \
        f"The title for active devices does not match 'Active' (found: '{active_controllers_title}')."

    # STEP 2: Retrieve and validate the count of active controllers
    active_controllers_count = sanitize_count(hce.active_devices_count.get_text)
    assert active_controllers_count > 0, \
        f"The count of active devices should be greater than 0 (found: {active_controllers_count})."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1961")
@qase_test(case_id=1961)  # Use the decorator for Qase integration
def test_dashboard_inactive_devices(driver_uk_prod_login_admin, run_id):
    """
    Verify that "Inactive" controllers are being shown on the dashboard.
    """

    # Initialize page objects
    hce = HomePageControllers(driver_uk_prod_login_admin)

    # STEP 1: Verify the title for inactive devices
    inactive_controllers_title = hce.inactive_devices_title.get_text
    assert inactive_controllers_title == "Inactive", \
        f"Expected 'Inactive', but got '{inactive_controllers_title}'."

    # STEP 2: Retrieve and validate the count of inactive controllers
    inactive_controllers_count = sanitize_count(hce.inactive_devices_count.get_text)
    assert inactive_controllers_count > 0, \
        f"Expected inactive devices count to be greater than 0, but got {inactive_controllers_count}."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1962")
@qase_test(case_id=1962)  # Use the decorator for Qase integration
def test_dashboard_fault_devices(driver_uk_prod_login_admin, run_id):
    """
    Verify that "Fault" controllers are being displayed on the dashboard.
    """

    # Initialize page objects
    hce = HomePageControllers(driver_uk_prod_login_admin)

    # STEP 1: Verify the title for fault devices
    fault_devices_title = hce.fault_devices_title.get_text
    assert fault_devices_title == "Fault", \
        f"Expected 'Fault', but got '{fault_devices_title}'."

    # STEP 2: Retrieve and validate the count of fault devices
    fault_devices_count = sanitize_count(hce.fault_devices_count.get_text)
    assert fault_devices_count > 0, \
        f"Expected fault devices count to be greater than 0, but got {fault_devices_count}."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1963")
@qase_test(case_id=1963)  # Use the decorator for Qase integration
def test_dashboard_unknown_status(driver_uk_prod_login_admin, run_id):
    """
    Verify that "Unknown status" controllers are being displayed on the dashboard.
    """

    # Initialize page objects
    hce = HomePageControllers(driver_uk_prod_login_admin)

    # STEP 1: Verify the label for "Unknown status" devices
    unknown_status_label = hce.unknown_status_devices_title.get_text
    assert unknown_status_label == "Unknown status", \
        "The label for 'Unknown status' is incorrect or not displayed."

    # STEP 2: Retrieve and validate the count of "Unknown status" devices
    unknown_status_count = sanitize_count(hce.unknown_status_devices_count.get_text)
    assert unknown_status_count > 0, \
        f"The count of 'Unknown status' devices is {unknown_status_count}, which is not greater than 0."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1964")
@qase_test(case_id=1964)  # Use the decorator for Qase integration
def test_dashboard_active_controllers(driver_uk_prod_login_admin, run_id):
    """
    Verify that the "Active" controllers number is higher than 10K.
    """

    # Initialize page objects
    hce = HomePageControllers(driver_uk_prod_login_admin)

    # STEP 1: Verify the title for active controllers
    active_controllers_title = hce.active_devices_title.get_text
    assert active_controllers_title == "Active", \
        f"Expected 'Active', but got '{active_controllers_title}'."

    # STEP 2: Retrieve and validate the count of active controllers
    active_controllers_count = sanitize_count(hce.active_devices_count.get_text)
    assert active_controllers_count > 10000, \
        f"Expected active controllers count to be greater than 10,000, but got {active_controllers_count}."


# HOMEPAGE DASHBOARD -> DEVICES -> HEADSETS
@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1969")
@qase_test(case_id=1969)  # Use the decorator for Qase integration
@mark.workingon
def test_dashboard_headsets(driver_uk_prod_login_admin, run_id):
    """
    Verify that the headsets module displays all necessary data
    (online, offline, offline for more than 30 days, and unknown).
    """

    # Initialize page objects
    hm = HomePageHeadsetsModal(driver_uk_prod_login_admin)

    # Define the expected labels and associate them with corresponding elements
    labels_and_counts = {
        "online": ("Online", hm.online_label, hm.online_count),
        "offline": ("Offline", hm.offline_label, hm.offline_count),
        "long offline": ("Offline for more than 30 days", hm.long_offline_label, hm.long_offline_count),
        "unknown": ("Unknown", hm.unknown_label, hm.unknown_count)
    }

    # Verify each label and count dynamically
    for label_name, (expected_text, label_element, count_element) in labels_and_counts.items():
        # Verify that the label is displayed with the correct text
        label_text = label_element.get_text
        assert label_text == expected_text, \
            f"Expected '{expected_text}' label for {label_name}, but got '{label_text}'."

        # Verify that the count is greater than zero
        count = sanitize_count(count_element.get_text)
        assert count > 0, \
            f"Expected {label_name} count to be greater than 0, but got {count}."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1970")
@qase_test(case_id=1970)  # Use the decorator for Qase integration
def test_navigate_to_headsets_details_page_from_dashboard(driver_uk_prod_login_admin, run_id):
    """
    Verify that the user is able to click on the "Headsets" section,
    and they get redirected to the Headsets details page.
    """

    # Initialize page objects
    hm = HomePageHeadsetsModal(driver_uk_prod_login_admin)
    hd = HeadsetsDetailsPage(driver_uk_prod_login_admin)

    # STEP 1: Click on the "Headsets" section in the modal.
    # EXPECTED RESULT: The system should navigate to the Headsets details page.
    hm.headsets_modal_title.click()

    # STEP 2: Verify that the Headsets details page title is displayed.
    # EXPECTED RESULT: The Headsets details page title element should be visible.
    assert hd.headsets_details_page_title.is_displayed(), \
        "The Headsets details page title is not displayed."

    # STEP 3: Verify that the Headsets details page title contains the word "Headset".
    # EXPECTED RESULT: The text of the Headsets details page title should include "Headset".
    assert "Headset" in hd.headsets_details_page_title.get_text, \
        "The Headsets details page title does not contain 'Headset'."


# HOMEPAGE DASHBOARD -> DEVICES -> HANDSETS
@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1971")
@qase_test(case_id=1971)  # Use the decorator for Qase integration
def test_dashboard_handsets(driver_uk_prod_login_admin, run_id):
    """
    Verify that the handsets module displays all necessary data
    (online, offline, offline for more than 30 days, and unknown).
    """

    # Initialize page objects
    hndset = HomePageHandsetsModal(driver_uk_prod_login_admin)

    # Define expected labels and counts
    labels_and_counts = {
        "online": ("Online", hndset.online_label, hndset.online_count),
        "offline": ("Offline", hndset.offline_label, hndset.offline_count),
        "long offline": ("Offline for more than 30 days", hndset.long_offline_label, hndset.long_offline_count),
        "unknown": ("Unknown", hndset.unknown_label, hndset.unknown_count)
    }

    # Dynamically verify labels and counts
    for label_name, (expected_text, label_element, count_element) in labels_and_counts.items():
        # Verify that the label is displayed with the correct text
        label_text = label_element.get_text
        assert label_text == expected_text, \
            f"Expected '{expected_text}' label for {label_name}, but got '{label_text}'."

        # Verify that the count is greater than zero
        count = sanitize_count(count_element.get_text)
        assert count > 0, \
            f"Expected {label_name} count to be greater than 0, but got {count}."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1972")
@qase_test(case_id=1972)  # Use the decorator for Qase integration
def test_navigate_to_handsets_details_page_from_dashboard(driver_uk_prod_login_admin, run_id):
    """
    Verify that the user is able to click on the "Handsets" section,
    and they get redirected to the Handsets details page.
    """

    # Initialize page objects
    hm = HomePageHandsetsModal(driver_uk_prod_login_admin)
    hd = HandsetsDetailsPage(driver_uk_prod_login_admin)

    # STEP 1: Click on the "Handsets" section in the modal
    hm.handsets_modal_title.click()

    # STEP 2: Verify that the Handsets details page title is displayed
    assert hd.handsets_details_page_title.is_displayed(), \
        "The Handsets details page title is not displayed."

    # STEP 3: Verify that the Handsets page title contains the word "Handset"
    assert "Handset" in hd.handsets_details_page_title.get_text, \
        "Expected to navigate to the Handsets details page, but navigated elsewhere."


# HOMEPAGE DASHBOARD -> DEVICES -> CALL POINTS
@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1973")
@qase_test(case_id=1973)  # Use the decorator for Qase integration
def test_dashboard_callpoints(driver_uk_prod_login_admin, run_id):
    """
    Verify that the call points module displays all necessary data
    (online, offline, offline for more than 30 days, and unknown).
    """

    # Initialize page objects
    callpoints = HomePageCallPointsModal(driver_uk_prod_login_admin)

    # Define expected labels and counts
    labels_and_counts = {
        "online": ("Online", callpoints.online_label, callpoints.online_count),
        "offline": ("Offline", callpoints.offline_label, callpoints.offline_count),
        "long offline": ("Offline for more than 30 days", callpoints.long_offline_label, callpoints.long_offline_count),
        "unknown": ("Unknown", callpoints.unknown_label, callpoints.unknown_count)
    }

    # Dynamically verify labels and counts
    for label_name, (expected_text, label_element, count_element) in labels_and_counts.items():
        # Verify that the label is displayed with the correct text
        label_text = label_element.get_text
        assert label_text == expected_text, \
            f"Expected '{expected_text}' label for {label_name}, but got '{label_text}'."

        # Verify that the count is greater than zero
        count = sanitize_count(count_element.get_text)  # Use sanitize_count to ensure an integer
        assert count > 0, \
            f"Expected {label_name} count to be greater than 0, but got {count}."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1974")
@qase_test(case_id=1974)  # Use the decorator for Qase integration
def test_navigate_to_callpoints_details_page_from_dashboard(driver_uk_prod_login_admin, run_id):
    """
    Verify that the user is able to click on the "Call Points" section,
    and they get redirected to the Call Points details page.
    """

    # Initialize page objects
    cp = HomePageCallPointsModal(driver_uk_prod_login_admin)
    cd = CallPointsDetailsPage(driver_uk_prod_login_admin)

    # STEP 1: Click on the "Call Points" section in the modal
    cp.callpoints_modal_title.click()

    # STEP 2: Verify that the Call Points details page title is displayed
    assert cd.callpoints_details_page_title.is_displayed(), \
        "The Call Points details page title is not displayed."

    # STEP 3: Verify that the Call Points page title contains the word "Call Points"
    assert "Call Points" in cd.callpoints_details_page_title.get_text, \
        "Expected to navigate to the Call Points details page, but navigated elsewhere."


# HOMEPAGE DASHBOARD -> DEVICES -> KEYPADS
@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1975")
@qase_test(case_id=1975)  # Use the decorator for Qase integration
def test_dashboard_keypads(driver_uk_prod_login_admin, run_id):
    """
    Verify that the keypads module displays all necessary data
    (online, offline, offline for more than 30 days, and unknown).
    """

    # Initialize page objects
    keypads = HomePageKeyPadsModal(driver_uk_prod_login_admin)

    # Define expected labels and counts
    labels_and_counts = {
        "online": ("Online", keypads.online_label, keypads.online_count),
        "offline": ("Offline", keypads.offline_label, keypads.offline_count),
        "long offline": ("Offline for more than 30 days", keypads.long_offline_label, keypads.long_offline_count),
        "unknown": ("Unknown", keypads.unknown_label, keypads.unknown_count)
    }

    # Dynamically verify labels and counts
    for label_name, (expected_text, label_element, count_element) in labels_and_counts.items():
        # Verify that the label is displayed with the correct text
        label_text = label_element.get_text
        assert label_text == expected_text, \
            f"Expected '{expected_text}' label for {label_name}, but got '{label_text}'."

        # Verify that the count is greater than zero
        try:
            count = int(count_element.get_text)  # Directly cast to int
            assert count > 0, \
                f"Expected {label_name} count to be greater than 0, but got {count}."
        except ValueError:
            raise AssertionError(f"Failed to convert {label_name} count '{count_element.get_text}' to an integer.")


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1976")
@qase_test(case_id=1976)  # Use the decorator for Qase integration
def test_navigate_to_keypads_details_page_from_dashboard(driver_uk_prod_login_admin, run_id):
    """
    Verify that the user is able to click on the "Keypads"
    section, and they get redirected to the Keypads details page.
    """

    # Initialize page objects
    hmkp = HomePageKeyPadsModal(driver_uk_prod_login_admin)
    kp = KeypadsDetailsPage(driver_uk_prod_login_admin)

    # STEP 1: Click on the "Keypads" section in the modal
    hmkp.keypads_modal_title.click()

    # STEP 2: Verify that the Keypads details page title is displayed
    assert kp.keypads_details_page_title.is_displayed(), \
        "The Keypads details page title is not displayed."

    # STEP 3: Verify that the Keypads page title contains the word "Keypads"
    assert "Keypads" in kp.keypads_details_page_title.get_text, \
        "Expected to navigate to the Keypads details page, but navigated elsewhere."
