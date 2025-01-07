from locators import (HomePageControllers, HomePageHeadsetsModal, HeadsetsDetailsPage, HomePageHandsetsModal,
                      HandsetsDetailsPage, HomePageCallPointsModal, HomePageKeyPadsModal, CallPointsDetailsPage,
                      KeypadsDetailsPage, HomePage)
from pytest import mark
import time
from conftest import qase_test
from conftest import sanitize_count


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1965")
@qase_test(case_id=1965)  # Use the decorator for Qase integration
def test_filtering_by_group_internal_vocovo(driver_uk_prod_login_admin, run_id):
    """Verify that filtering works by selecting a group (Vocovo Internal)."""

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    hpc = HomePageControllers(driver_uk_prod_login_admin)

    # STEP 1: Verify the base filter title is "Strongbyte Solutions Ltd"
    base_filter_title = homepage.dropdown_button.get_text
    assert base_filter_title == "Strongbyte Solutions Ltd", (
        f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
    )

    # STEP 2: Retrieve the number of active devices on the default dashboard
    default_page_headsets_active_number = hpc.active_devices_count.get_text

    # STEP 3: Open the dropdown menu
    homepage.dropdown_button.click()

    # STEP 4: Type "Vocovo Internal" into the input field
    homepage.dropdown_input.send_keys("Vocovo Internal")

    # STEP 5: Select the "Vocovo Internal" option from the dropdown
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 6: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 7: Retrieve the number of active devices for the "Vocovo Internal" group
    vocovo_internal_active_number = hpc.active_devices_count.get_text

    # STEP 8: Verify that the active devices count changes after filtering
    assert default_page_headsets_active_number != vocovo_internal_active_number, \
        "The active devices count did not change after applying the filter."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1977")
@qase_test(case_id=1977)  # Use the decorator for Qase integration
def test_filtering_by_group_internal_vocovo_active_controllers(driver_uk_prod_login_admin, run_id):
    """
    After filtering by selecting a group, the "Active" controllers belonging
    to that group are being shown on the dashboard.
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    hpc = HomePageControllers(driver_uk_prod_login_admin)

    # STEP 1: Verify the base filter title is "Strongbyte Solutions Ltd"
    base_filter_title = homepage.dropdown_button.get_text
    assert base_filter_title == "Strongbyte Solutions Ltd", (
        f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
    )

    # STEP 2: Retrieve the number of active devices on the default dashboard
    default_page_headsets_active_number = hpc.active_devices_count.get_text

    # STEP 3: Open the dropdown menu
    homepage.dropdown_button.click()

    # STEP 4: Type "Vocovo Internal" into the input field
    homepage.dropdown_input.send_keys("Vocovo Internal")

    # STEP 5: Select the "Vocovo Internal" option from the dropdown
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 6: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 7: Retrieve the number of active devices for the "Vocovo Internal" group
    vocovo_internal_active_number = hpc.active_devices_count.get_text

    # STEP 8: Verify that the active devices count changes after filtering
    assert default_page_headsets_active_number != vocovo_internal_active_number, \
        "The active devices count did not change after applying the filter."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1978")
@qase_test(case_id=1978)  # Use the decorator for Qase integration
def test_filtering_by_group_internal_vocovo_inactive_controllers(driver_uk_prod_login_admin, run_id):
    """
    After filtering by selecting a group, the "Inactive" controllers belonging
    to that group are being shown on the dashboard.
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    hpc = HomePageControllers(driver_uk_prod_login_admin)

    # STEP 1: Verify the base filter title is "Strongbyte Solutions Ltd"
    base_filter_title = homepage.dropdown_button.get_text
    assert base_filter_title == "Strongbyte Solutions Ltd", (
        f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
    )

    # STEP 2: Retrieve the number of inactive devices on the default dashboard
    default_page_headsets_inactive_number = hpc.inactive_devices_count.get_text

    # STEP 3: Open the dropdown menu
    homepage.dropdown_button.click()

    # STEP 4: Type "Vocovo Internal" into the input field
    homepage.dropdown_input.send_keys("Vocovo Internal")

    # STEP 5: Select the "Vocovo Internal" option from the dropdown
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 6: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 7: Retrieve the number of inactive devices for the "Vocovo Internal" group
    vocovo_internal_inactive_number = hpc.inactive_devices_count.get_text

    # STEP 8: Verify that the inactive devices count changes after filtering
    assert default_page_headsets_inactive_number != vocovo_internal_inactive_number, \
        "The inactive devices count did not change after applying the filter."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1979")
@qase_test(case_id=1979)  # Use the decorator for Qase integration
def test_filtering_by_group_internal_vocovo_fault_controllers(driver_uk_prod_login_admin, run_id):
    """
    After filtering by selecting a group, the "Fault" controllers belonging
    to that group are being shown on the dashboard.
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    hpc = HomePageControllers(driver_uk_prod_login_admin)

    # STEP 1: Verify the base filter title is "Strongbyte Solutions Ltd"
    base_filter_title = homepage.dropdown_button.get_text
    assert base_filter_title == "Strongbyte Solutions Ltd", (
        f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
    )

    # STEP 2: Retrieve the default number of fault devices
    default_page_headsets_fault_number = hpc.fault_devices_title.get_text

    # STEP 3: Open the dropdown menu
    homepage.dropdown_button.click()

    # STEP 4: Type "Vocovo Internal" into the input field
    homepage.dropdown_input.send_keys("Vocovo Internal")

    # STEP 5: Select the "Vocovo Internal" option from the dropdown
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 6: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 7: Verify that the number of fault devices changes after filtering
    vocovo_internal_fault_number = hpc.fault_devices_count.get_text
    assert default_page_headsets_fault_number != vocovo_internal_fault_number, (
        f"Expected fault devices count to change, but it remained {default_page_headsets_fault_number}."
    )
    
    
@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1980")
@qase_test(case_id=1980)  # Use the decorator for Qase integration
def test_filtering_by_group_internal_vocovo_unknown_status_controllers(driver_uk_prod_login_admin, run_id):
    """
    After filtering by selecting a group, the "Unknown status" controllers are
    being displayed on the dashboard.
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    hpc = HomePageControllers(driver_uk_prod_login_admin)

    # STEP 1: Verify the base filter title is "Strongbyte Solutions Ltd"
    base_filter_title = homepage.dropdown_button.get_text
    assert base_filter_title == "Strongbyte Solutions Ltd", (
        f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
    )

    # STEP 2: Retrieve the default number of "Unknown status" devices
    default_page_headsets_unknown_status_number = hpc.unknown_status_devices_count.get_text

    # STEP 3: Open the dropdown menu
    homepage.dropdown_button.click()

    # STEP 4: Type "Vocovo Internal" into the input field
    homepage.dropdown_input.send_keys("Vocovo Internal")

    # STEP 5: Select the "Vocovo Internal" option from the dropdown
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 6: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 7: Retrieve the number of "Unknown status" devices for the "Vocovo Internal" group
    vocovo_internal_unknown_number = hpc.unknown_status_devices_count.get_text

    # STEP 8: Verify that the "Unknown status" devices count changes after filtering
    assert default_page_headsets_unknown_status_number != vocovo_internal_unknown_number, \
        f"Expected 'Unknown status' devices count to change, but it remained {default_page_headsets_unknown_status_number}."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1981")
@qase_test(case_id=1981)  # Use the decorator for Qase integration
def test_filtering_by_group_internal_vocovo_headset_modal(driver_uk_prod_login_admin, run_id):
    """
    Verify that the headsets module displays all necessary data for the
    selected group (online, offline, offline for more than 30 days, and unknown).
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    hphm = HomePageHeadsetsModal(driver_uk_prod_login_admin)

    # STEP 1: Verify the base filter title is "Strongbyte Solutions Ltd"
    base_filter_title = homepage.dropdown_button.get_text
    assert base_filter_title == "Strongbyte Solutions Ltd", (
        f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
    )

    # STEP 2: Retrieve the default number of headsets by status
    default_page_online_headsets = sanitize_count(hphm.online_count.get_text)
    default_page_offline_headsets = sanitize_count(hphm.offline_count.get_text)
    default_page_offline_30_days = sanitize_count(hphm.long_offline_count.get_text)
    default_page_unknown_headsets = sanitize_count(hphm.unknown_count.get_text)

    # STEP 3: Open the dropdown menu and filter by "Vocovo Internal"
    homepage.dropdown_button.click()
    homepage.dropdown_input.send_keys("Vocovo Internal")
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 4: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 5: Retrieve the number of headsets for "Vocovo Internal" by status
    vocovo_internal_page_online_headsets = sanitize_count(hphm.online_count.get_text)
    vocovo_internal_page_offline_headsets = sanitize_count(hphm.offline_count.get_text)
    vocovo_internal_page_offline_30_days = sanitize_count(hphm.long_offline_count.get_text)
    vocovo_internal_page_unknown_headsets = sanitize_count(hphm.unknown_count.get_text)

    # STEP 6: Verify the number of headsets changes after filtering
    assert default_page_online_headsets != vocovo_internal_page_online_headsets, \
        "Online headsets count did not change after filtering."
    assert default_page_offline_headsets != vocovo_internal_page_offline_headsets, \
        "Offline headsets count did not change after filtering."
    assert default_page_offline_30_days != vocovo_internal_page_offline_30_days, \
        "Headsets offline for more than 30 days count did not change after filtering."
    assert default_page_unknown_headsets != vocovo_internal_page_unknown_headsets, \
        "Unknown headsets count did not change after filtering."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1982")
@qase_test(case_id=1982)  # Use the decorator for Qase integration
def test_navigate_to_the_headsets_module_details_page_for_a_group(driver_uk_prod_login_admin, run_id):
    """
    Verify that clicking on the headsets module will redirect the user to the
    headsets details page for the selected group.
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    hphm = HomePageHeadsetsModal(driver_uk_prod_login_admin)
    headset_details = HeadsetsDetailsPage(driver_uk_prod_login_admin)

    # STEP 1: Retrieve the default number of headsets by status
    default_page_online_headsets = sanitize_count(hphm.online_count.get_text)
    default_page_offline_headsets = sanitize_count(hphm.offline_count.get_text)
    default_page_offline_30_days = sanitize_count(hphm.long_offline_count.get_text)
    default_page_unknown_headsets = sanitize_count(hphm.unknown_count.get_text)

    # STEP 2: Open the dropdown menu and filter by "Vocovo Internal"
    homepage.dropdown_button.click()
    homepage.dropdown_input.send_keys("Vocovo Internal")
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 3: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 4: Retrieve the number of headsets for "Vocovo Internal" by status
    vocovo_internal_page_online_headsets = sanitize_count(hphm.online_count.get_text)
    vocovo_internal_page_offline_headsets = sanitize_count(hphm.offline_count.get_text)
    vocovo_internal_page_offline_30_days = sanitize_count(hphm.long_offline_count.get_text)
    vocovo_internal_page_unknown_headsets = sanitize_count(hphm.unknown_count.get_text)

    # STEP 5: Verify the number of headsets changes after filtering
    assert default_page_online_headsets != vocovo_internal_page_online_headsets, \
        "Online headsets count did not change after filtering."
    assert default_page_offline_headsets != vocovo_internal_page_offline_headsets, \
        "Offline headsets count did not change after filtering."
    assert default_page_offline_30_days != vocovo_internal_page_offline_30_days, \
        "Headsets offline for more than 30 days count did not change after filtering."
    assert default_page_unknown_headsets != vocovo_internal_page_unknown_headsets, \
        "Unknown headsets count did not change after filtering."

    # STEP 6: Navigate to the headsets details page
    hphm.headsets_modal_title.click()
    assert "Headsets" in headset_details.headsets_details_page_title.get_text, \
        "The headsets details page title does not contain 'Headsets'."

    # STEP 7: Verify that the headsets details page belongs to the "VoCoVo Internal" group
    online_headsets = sanitize_count(headset_details.online_count.get_text)
    offline_headsets = sanitize_count(headset_details.offline_count.get_text)
    offline_for_more = sanitize_count(headset_details.long_offline_count.get_text)
    unknown_headsets = sanitize_count(headset_details.unknown_count.get_text)

    assert vocovo_internal_page_online_headsets == online_headsets, \
        "Online headsets count does not match on the details page."
    assert vocovo_internal_page_offline_headsets == offline_headsets, \
        "Offline headsets count does not match on the details page."
    assert vocovo_internal_page_offline_30_days == offline_for_more, \
        "Headsets offline for more than 30 days count does not match on the details page"


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1983")
@qase_test(case_id=1983)  # Use the decorator for Qase integration
def test_filtering_by_group_internal_vocovo_handsets_modal(driver_uk_prod_login_admin, run_id):
    """
    Verify that the handsets module displays all necessary data for the selected group
    (online, offline, offline for more than 30 days, and unknown).
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    handsets = HomePageHandsetsModal(driver_uk_prod_login_admin)

    # STEP 1: Verify the base filter title is "Strongbyte Solutions Ltd"
    base_filter_title = homepage.dropdown_button.get_text
    assert base_filter_title == "Strongbyte Solutions Ltd", (
        f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
    )

    # STEP 2: Retrieve the default number of handsets by category
    default_page_online_handsets = sanitize_count(handsets.online_count.get_text)
    default_page_offline_handsets = sanitize_count(handsets.offline_count.get_text)
    default_page_offline_30_days = sanitize_count(handsets.long_offline_count.get_text)
    default_page_unknown_handsets = sanitize_count(handsets.unknown_count.get_text)

    # STEP 3: Open the dropdown menu
    homepage.dropdown_button.click()

    # STEP 4: Type "Vocovo Internal" into the input field
    homepage.dropdown_input.send_keys("Vocovo Internal")

    # STEP 5: Select the "Vocovo Internal" option from the dropdown
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 6: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 7: Retrieve the number of handsets for "Vocovo Internal" by category
    vocovo_internal_page_online_handsets = sanitize_count(handsets.online_count.get_text)
    vocovo_internal_page_offline_handsets = sanitize_count(handsets.offline_count.get_text)
    vocovo_internal_page_offline_30_days = sanitize_count(handsets.long_offline_count.get_text)
    vocovo_internal_page_unknown_handsets = sanitize_count(handsets.unknown_count.get_text)

    # STEP 8: Verify the number of handsets changes after filtering
    assert default_page_online_handsets != vocovo_internal_page_online_handsets, \
        "Online handsets count did not change after filtering."
    assert default_page_offline_handsets != vocovo_internal_page_offline_handsets, \
        "Offline handsets count did not change after filtering."
    assert default_page_offline_30_days != vocovo_internal_page_offline_30_days, \
        "Handsets offline for more than 30 days count did not change after filtering."
    assert default_page_unknown_handsets != vocovo_internal_page_unknown_handsets, \
        "Unknown handsets count did not change after filtering."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1984")
@qase_test(case_id=1984)  # Use the decorator for Qase integration
def test_navigate_to_the_handsets_module_details_page_for_a_group(driver_uk_prod_login_admin, run_id):
    """
    Verify that clicking on the handsets module will redirect the user to the
    handsets details page for the selected group.
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    handsetshomepage = HomePageHandsetsModal(driver_uk_prod_login_admin)
    handset_details = HandsetsDetailsPage(driver_uk_prod_login_admin)

    # STEP 1: Retrieve the default number of handsets by category
    default_page_online_handsets = sanitize_count(handsetshomepage.online_count.get_text)
    default_page_offline_handsets = sanitize_count(handsetshomepage.offline_count.get_text)
    default_page_offline_30_days = sanitize_count(handsetshomepage.long_offline_count.get_text)
    default_page_unknown_handsets = sanitize_count(handsetshomepage.unknown_count.get_text)

    # STEP 2: Open the dropdown menu and filter by "Vocovo Internal"
    homepage.dropdown_button.click()
    homepage.dropdown_input.send_keys("Vocovo Internal")
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 3: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 4: Retrieve the number of handsets for "Vocovo Internal" by category
    vocovo_internal_page_online_handsets = sanitize_count(handsetshomepage.online_count.get_text)
    vocovo_internal_page_offline_handsets = sanitize_count(handsetshomepage.offline_count.get_text)
    vocovo_internal_page_offline_30_days = sanitize_count(handsetshomepage.long_offline_count.get_text)
    vocovo_internal_page_unknown_handsets = sanitize_count(handsetshomepage.unknown_count.get_text)

    # STEP 5: Verify the number of handsets changes after filtering
    assert default_page_online_handsets != vocovo_internal_page_online_handsets, \
        "Online handsets count did not change after filtering."
    assert default_page_offline_handsets != vocovo_internal_page_offline_handsets, \
        "Offline handsets count did not change after filtering."
    assert default_page_offline_30_days != vocovo_internal_page_offline_30_days, \
        "Handsets offline for more than 30 days count did not change after filtering."
    assert default_page_unknown_handsets != vocovo_internal_page_unknown_handsets, \
        "Unknown handsets count did not change after filtering."

    # STEP 6: Navigate to the handsets details page
    handsetshomepage.handsets_modal_title.click()
    assert "Handsets" in handset_details.handsets_details_page_title.get_text, \
        "The handsets details page title does not contain 'Handsets'."

    # STEP 7: Verify the handsets details page data matches the Vocovo Internal group
    online_handsets = sanitize_count(handset_details.online_count.get_text)
    offline_handsets = sanitize_count(handset_details.offline_count.get_text)
    offline_for_more = sanitize_count(handset_details.long_offline_count.get_text)
    unknown_handsets = sanitize_count(handset_details.unknown_count.get_text)

    assert vocovo_internal_page_online_handsets == online_handsets, \
        "Online handsets count does not match on the details page."
    assert vocovo_internal_page_offline_handsets == offline_handsets, \
        "Offline handsets count does not match on the details page."
    assert vocovo_internal_page_offline_30_days == offline_for_more, \
        "Handsets offline for more than 30 days count does not match on the details page."
    assert vocovo_internal_page_unknown_handsets == unknown_handsets, \
        "Unknown handsets count does not match on the details page."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1985")
@qase_test(case_id=1985)  # Use the decorator for Qase integration
def test_filtering_by_group_internal_vocovo_callpoints_modal(driver_uk_prod_login_admin, run_id):
    """
    Verify that the call points module displays all necessary data for the
    selected group (online, offline, offline for more than 30 days, and unknown).
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    callpoints = HomePageCallPointsModal(driver_uk_prod_login_admin)

    # STEP 1: Verify the base filter title is "Strongbyte Solutions Ltd"
    base_filter_title = homepage.dropdown_button.get_text
    assert base_filter_title == "Strongbyte Solutions Ltd", (
        f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
    )

    # STEP 2: Retrieve the default number of call points by category
    default_page_online_callpoints = callpoints.online_count.get_text
    default_page_offline_callpoints = callpoints.offline_count.get_text
    default_page_offline_30_days = callpoints.long_offline_count.get_text
    default_page_unknown_callpoints = callpoints.unknown_count.get_text

    # STEP 3: Open the dropdown menu and filter by "Vocovo Internal"
    homepage.dropdown_button.click()
    homepage.dropdown_input.send_keys("Vocovo Internal")
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 4: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 5: Retrieve the number of call points for "Vocovo Internal" by category
    vocovo_internal_page_online_callpoints = callpoints.online_count.get_text
    vocovo_internal_page_offline_callpoints = callpoints.offline_count.get_text
    vocovo_internal_page_offline_30_days = callpoints.long_offline_count.get_text
    vocovo_internal_page_unknown_callpoints = callpoints.unknown_count.get_text

    # STEP 6: Verify the number of call points changes after filtering
    assert default_page_online_callpoints != vocovo_internal_page_online_callpoints, \
        "Online call points count did not change after filtering."
    assert default_page_offline_callpoints != vocovo_internal_page_offline_callpoints, \
        "Offline call points count did not change after filtering."
    assert default_page_offline_30_days != vocovo_internal_page_offline_30_days, \
        "Call points offline for more than 30 days count did not change after filtering."
    assert default_page_unknown_callpoints != vocovo_internal_page_unknown_callpoints, \
        "Unknown call points count did not change after filtering."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1986")
@qase_test(case_id=1986)  # Use the decorator for Qase integration
@mark.workingon
def test_navigate_to_the_callpoints_module_details_page_for_a_group(driver_uk_prod_login_admin, run_id):
    """
    Verify that clicking on the call points module will redirect
    the user to the call points details page for that group.
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    callpoints_home = HomePageCallPointsModal(driver_uk_prod_login_admin)
    callpoints_details = CallPointsDetailsPage(driver_uk_prod_login_admin)

    # STEP 1: Retrieve the default number of call points by category
    default_page_online_callpoints = sanitize_count(callpoints_home.online_count.get_text)
    default_page_offline_callpoints = sanitize_count(callpoints_home.offline_count.get_text)
    default_page_offline_30_days = sanitize_count(callpoints_home.long_offline_count.get_text)
    default_page_unknown_callpoints = sanitize_count(callpoints_home.unknown_count.get_text)

    # STEP 2: Open the dropdown menu and filter by "Vocovo Internal"
    homepage.dropdown_button.click()
    homepage.dropdown_input.send_keys("Vocovo Internal")
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 3: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 4: Retrieve the number of call points for "Vocovo Internal" by category
    vocovo_internal_page_online_callpoints = sanitize_count(callpoints_home.online_count.get_text)
    vocovo_internal_page_offline_callpoints = sanitize_count(callpoints_home.offline_count.get_text)
    vocovo_internal_page_offline_30_days = sanitize_count(callpoints_home.long_offline_count.get_text)
    vocovo_internal_page_unknown_callpoints = sanitize_count(callpoints_home.unknown_count.get_text)

    # STEP 5: Verify the number of call points changes after filtering
    assert default_page_online_callpoints != vocovo_internal_page_online_callpoints, \
        "Online call points count did not change after filtering."
    assert default_page_offline_callpoints != vocovo_internal_page_offline_callpoints, \
        "Offline call points count did not change after filtering."
    assert default_page_offline_30_days != vocovo_internal_page_offline_30_days, \
        "Call points offline for more than 30 days count did not change after filtering."
    assert default_page_unknown_callpoints != vocovo_internal_page_unknown_callpoints, \
        "Unknown call points count did not change after filtering."

    # STEP 6: Navigate to the call points details page
    callpoints_home.callpoints_modal_title.click()
    assert "Call Points" in callpoints_details.callpoints_details_page_title.get_text, \
        "The call points details page title does not contain 'Call Points'."

    # STEP 7: Verify the call points details page data matches the Vocovo Internal group
    online_callpoints = sanitize_count(callpoints_details.online_count.get_text)
    offline_callpoints = sanitize_count(callpoints_details.offline_count.get_text)
    offline_for_more = sanitize_count(callpoints_details.long_offline_count.get_text)
    unknown_callpoints = sanitize_count(callpoints_details.unknown_count.get_text)

    assert vocovo_internal_page_online_callpoints == online_callpoints, \
        "Online call points count does not match on the details page."
    assert vocovo_internal_page_offline_callpoints == offline_callpoints, \
        "Offline call points count does not match on the details page."
    assert vocovo_internal_page_offline_30_days == offline_for_more, \
        "Call points offline for more than 30 days count does not match on the details page."
    assert vocovo_internal_page_unknown_callpoints == unknown_callpoints, \
        "Unknown call points count does not match on the details page."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1987")
@qase_test(case_id=1987)  # Use the decorator for Qase integration
def test_filtering_by_group_internal_vocovo_keypads_modal(driver_uk_prod_login_admin, run_id):
    """
    Verify that the keypads module displays all necessary data for the
    selected group (online, offline, offline for more than 30 days, and unknown).
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    keypads = HomePageKeyPadsModal(driver_uk_prod_login_admin)

    # STEP 1: Verify the base filter title is "Strongbyte Solutions Ltd"
    base_filter_title = homepage.dropdown_button.get_text
    assert base_filter_title == "Strongbyte Solutions Ltd", (
        f"Expected 'Strongbyte Solutions Ltd', but got '{base_filter_title}'"
    )

    # STEP 2: Retrieve the default number of keypads by category
    default_page_online_keypads = sanitize_count(keypads.online_count.get_text)
    default_page_offline_keypads = sanitize_count(keypads.offline_count.get_text)
    default_page_offline_30_days = sanitize_count(keypads.long_offline_count.get_text)
    default_page_unknown_keypads = sanitize_count(keypads.unknown_count.get_text)

    # STEP 3: Open the dropdown menu and filter by "Vocovo Internal"
    homepage.dropdown_button.click()
    homepage.dropdown_input.send_keys("Vocovo Internal")
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 4: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 5: Retrieve the number of keypads for "Vocovo Internal" by category
    vocovo_internal_page_online_keypads = sanitize_count(keypads.online_count.get_text)
    vocovo_internal_page_offline_keypads = sanitize_count(keypads.offline_count.get_text)
    vocovo_internal_page_offline_30_days = sanitize_count(keypads.long_offline_count.get_text)
    vocovo_internal_page_unknown_keypads = sanitize_count(keypads.unknown_count.get_text)

    # STEP 6: Verify the number of keypads changes after filtering
    assert default_page_online_keypads != vocovo_internal_page_online_keypads, \
        "Online keypads count did not change after filtering."
    assert default_page_offline_keypads != vocovo_internal_page_offline_keypads, \
        "Offline keypads count did not change after filtering."
    assert default_page_offline_30_days != vocovo_internal_page_offline_30_days, \
        "Keypads offline for more than 30 days count did not change after filtering."
    assert default_page_unknown_keypads != vocovo_internal_page_unknown_keypads, \
        "Unknown keypads count did not change after filtering."


@mark.portaluksmoketests
@mark.regression
@mark.testcaseid("CE-1988")
@qase_test(case_id=1988)
def test_navigate_to_the_keypads_module_details_page_for_a_group(driver_uk_prod_login_admin, run_id):
    """
    Verify that clicking on the keypads module will redirect the user to the
    keypads details page for the selected group.
    """

    # Initialize page objects
    homepage = HomePage(driver_uk_prod_login_admin)
    keypads_home = HomePageKeyPadsModal(driver_uk_prod_login_admin)
    keypads_details = KeypadsDetailsPage(driver_uk_prod_login_admin)

    # STEP 1: Retrieve the default number of keypads by category
    default_page_online_keypads = sanitize_count(keypads_home.online_count.get_text)
    default_page_offline_keypads = sanitize_count(keypads_home.offline_count.get_text)
    default_page_offline_30_days = sanitize_count(keypads_home.long_offline_count.get_text)
    default_page_unknown_keypads = sanitize_count(keypads_home.unknown_count.get_text)

    # STEP 2: Open the dropdown menu and filter by "Vocovo Internal"
    homepage.dropdown_button.click()
    homepage.dropdown_input.send_keys("Vocovo Internal")
    homepage.dropdown_vocovo_internal_option.click()

    # STEP 3: Verify the filtering label displays "VoCoVo Internal"
    assert homepage.vocovo_internal_label_filtering.get_text == "VoCoVo Internal", \
        "The filtering label does not match the expected text."

    # STEP 4: Retrieve the number of keypads for "Vocovo Internal" by category
    vocovo_internal_page_online_keypads = sanitize_count(keypads_home.online_count.get_text)
    vocovo_internal_page_offline_keypads = sanitize_count(keypads_home.offline_count.get_text)
    vocovo_internal_page_offline_30_days = sanitize_count(keypads_home.long_offline_count.get_text)
    vocovo_internal_page_unknown_keypads = sanitize_count(keypads_home.unknown_count.get_text)

    # STEP 5: Verify the number of keypads changes after filtering
    assert default_page_online_keypads != vocovo_internal_page_online_keypads, \
        "Online keypads count did not change after filtering."
    assert default_page_offline_keypads != vocovo_internal_page_offline_keypads, \
        "Offline keypads count did not change after filtering."
    assert default_page_offline_30_days != vocovo_internal_page_offline_30_days, \
        "Keypads offline for more than 30 days count did not change after filtering."
    assert default_page_unknown_keypads != vocovo_internal_page_unknown_keypads, \
        "Unknown keypads count did not change after filtering."

    # STEP 6: Navigate to the keypads details page
    keypads_home.keypads_modal_title.click()
    assert "Keypads" in keypads_details.keypads_details_page_title.get_text, \
        "The keypads details page title does not contain 'Keypads'."

    # STEP 7: Verify the keypads details page data matches the Vocovo Internal group
    online_keypads = sanitize_count(keypads_details.online_count.get_text)
    offline_keypads = sanitize_count(keypads_details.offline_count.get_text)
    offline_for_more = sanitize_count(keypads_details.long_offline_count.get_text)
    unknown_keypads = sanitize_count(keypads_details.unknown_count.get_text)

    assert vocovo_internal_page_online_keypads == online_keypads, \
        "Online keypads count does not match on the details page."
    assert vocovo_internal_page_offline_keypads == offline_keypads, \
        "Offline keypads count does not match on the details page."
    assert vocovo_internal_page_offline_30_days == offline_for_more, \
        "Keypads offline for more than 30 days count does not match on the details page."
    assert vocovo_internal_page_unknown_keypads == unknown_keypads, \
        "Unknown keypads count does not match on the details page."
