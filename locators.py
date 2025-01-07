from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    input_email_field = (By.ID, "email")
    input_password_field = (By.ID, "password")
    login_button = (By.XPATH, "//button[span[text()='Log in']]")
    login_error_message = (By.XPATH, "//*[text()='Invalid username or password. Ensure your account is verified.']")
    forgot_password_link = (By.XPATH, "//*[text()='Forgot your password?']")


class ForgotPassword(BasePage):
    title_text = (By.XPATH, "//*[text()='Request password reset']")
    email_field = (By.ID, "email")
    request_reset_button = (By.XPATH, "//*[text()='Request reset']")
    return_to_login_page = (By.XPATH, "//*[text()='Return to login page']")
    request_successful_message = (By.XPATH, "//*[text()='Request successful']")
    info_message = (By.XPATH,
                    "//*[text()='Request successful. You should receive an email with "
                    "further instructions shortly (usually within 30 seconds).']")


class HomePage(BasePage):
    avatar_logo_button = (
        By.XPATH, "//span[@data-test='vocovo-avatar']//span[text()='QTV']"
    )
    profile_menu_item = (
        By.XPATH, "//a[text()='Profile']"
    )

    dropdown_button = (By.XPATH,
                       "//button[@data-test='group-button' and @class='ant-btn ant-btn-round ant-dropdown-trigger "
                       "group-button vocovo-button button-middle button-round  button-icon']")

    dropdown_input = (By.XPATH, "//input[@type='search' and @class='ant-select-selection-search-input']")

    dropdown_vocovo_internal_option = (By.XPATH, "//span[@class='ant-select-tree-title' and normalize-space(text())='VoCoVo Internal']")

    vocovo_internal_label_filtering = (By.XPATH, "//span[text()='VoCoVo Internal']")


class HomePageControllers(BasePage):
    # Map the title for the controllers section
    controllers_title = (
        By.XPATH,
        "//h3[@class='vocovo-map-header-label' and text()='Controllers']"
    )

    # Map the active devices card, allowing retrieval of both the count and title
    active_devices_count = (
        By.XPATH,
        "//div[@data-test='vocovo-online-stat-card']//div[@class='count']"
    )

    active_devices_title = (
        By.XPATH,
        "//div[@data-test='vocovo-online-stat-card']"
        "//div[@class='card-title' and text()='Active']"
    )

    # Map the inactive devices card
    inactive_devices_count = (
        By.XPATH,
        "//div[@data-test='vocovo-offline-stat-card']//div[@class='count']"
    )
    inactive_devices_title = (
        By.XPATH,
        "//div[@data-test='vocovo-offline-stat-card']"
        "//div[@class='card-title' and text()='Inactive']"
    )

    # Map the faulty devices card
    fault_devices_count = (
        By.XPATH,
        "//div[@data-test='vocovo-faulty-stat-card']//div[@class='count']"
    )
    fault_devices_title = (
        By.XPATH,
        "//div[@data-test='vocovo-faulty-stat-card']"
        "//div[@class='card-title' and text()='Fault']"
    )

    # Map the unknown status devices card
    unknown_status_devices_count = (
        By.XPATH,
        "//div[@data-test='vocovo-unknown-stat-card']//div[@class='count']"
    )
    unknown_status_devices_title = (
        By.XPATH,
        "//div[@data-test='vocovo-unknown-stat-card']"
        "//div[@class='card-title' and text()='Unknown status']"
    )


class HomePageHeadsetsModal(BasePage):
    offline_count = (
        By.XPATH,
        "//div[contains(@class, 'data-card-info-item-offline')]//div[contains(@class, 'data-card-info-item-value')]"
    )

    offline_label = (
        By.XPATH,
        "//div[@data-test='headset-dashboard-body']//span[contains(text(), 'Offline')]"
    )

    long_offline_count = (
        By.XPATH,
        "//div[@data-test='headset-dashboard-body']//div[contains(@class, 'data-card-info-item-longOffline')]"
        "//div[contains(@class, 'data-card-info-item-value')]"
    )

    long_offline_label = (
        By.XPATH,
        "//div[@data-test='headset-dashboard-body']//span[contains(text(), 'Offline for more than 30 days')]"
    )

    unknown_count = (
        By.XPATH,
        "//div[@data-test='headset-dashboard-body']//div[contains(@class, 'data-card-info-item-unknown')]"
        "//div[contains(@class, 'data-card-info-item-value')]"
    )

    unknown_label = (
        By.XPATH,
        "//div[@data-test='headset-dashboard-body']//span[contains(text(), 'Unknown')]"
    )

    online_count = (
        By.XPATH,
        "//div[@data-test='headset-dashboard-body']//div[contains(@class, 'data-card-info-item-online')]"
        "//div[contains(@class, 'data-card-info-item-value')]"
    )

    online_label = (
        By.XPATH,
        "//div[@data-test='headset-dashboard-body']//span[contains(text(), 'Online')]"
    )

    headsets_modal_title = (
        By.XPATH,
        "//div[@data-test='headset-dashboard-body']//span[@class='data-card-title' and contains(text(), 'Headsets')]"
    )


class HomePageHandsetsModal(BasePage):
    # Online elements
    online_count = (
        By.XPATH,
        "//div[@data-test='handset-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-online')]//div[@class='data-card-info-item-value']"
    )

    headsets_online_count = (
        By.XPATH,
        "//div[@data-test='handset-dashboard-body']//div[contains(@class, 'data-card-info-item-online')]"
        "//div[@class='data-card-info-item-value']"
    )
    online_label = (
        By.XPATH,
        "//div[@data-test='handset-dashboard-body']//span[text()='Online']"
    )

    # Offline elements
    offline_count = (
        By.XPATH,
        "//div[@data-test='handset-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-offline')]//div[@class='data-card-info-item-value']"
    )
    offline_label = (
        By.XPATH,
        "//div[@data-test='handset-dashboard-body']//span[text()='Offline']"
    )

    # Offline for more than 30 days elements
    long_offline_count = (
        By.XPATH,
        "//div[@data-test='handset-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-longOffline')]//div[@class='data-card-info-item-value']"
    )
    long_offline_label = (
        By.XPATH,
        "//div[@data-test='handset-dashboard-body']//span[text()='Offline for more than 30 days']"
    )

    # Unknown elements
    unknown_count = (
        By.XPATH,
        "//div[@data-test='handset-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-unknown')]//div[@class='data-card-info-item-value']"
    )
    unknown_label = (
        By.XPATH,
        "//div[@data-test='handset-dashboard-body']//span[text()='Unknown']"
    )

    handsets_modal_title = (
        By.XPATH,
        "//div[@data-test='handset-dashboard-body']//span[@class='data-card-title' and text()='Handsets']"
    )


class HomePageCallPointsModal(BasePage):
    # Online elements
    online_count = (
        By.XPATH,
        "//div[@data-test='callpoint-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-online')]//div[@class='data-card-info-item-value']"
    )
    online_label = (
        By.XPATH,
        "//div[@data-test='callpoint-dashboard-body']//span[text()='Online']"
    )

    # Offline elements
    offline_count = (
        By.XPATH,
        "//div[@data-test='callpoint-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-offline')]//div[@class='data-card-info-item-value']"
    )
    offline_label = (
        By.XPATH,
        "//div[@data-test='callpoint-dashboard-body']//span[text()='Offline']"
    )

    # Offline for more than 30 days elements
    long_offline_count = (
        By.XPATH,
        "//div[@data-test='callpoint-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-longOffline')]//div[@class='data-card-info-item-value']"
    )
    long_offline_label = (
        By.XPATH,
        "//div[@data-test='callpoint-dashboard-body']//span[text()='Offline for more than 30 days']"
    )

    # Unknown elements
    unknown_count = (
        By.XPATH,
        "//div[@data-test='callpoint-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-unknown')]//div[@class='data-card-info-item-value']"
    )
    unknown_label = (
        By.XPATH,
        "//div[@data-test='callpoint-dashboard-body']//span[text()='Unknown']"
    )

    callpoints_modal_title = (
        By.XPATH,
        "//div[@data-test='callpoint-dashboard-body']//span[@class='data-card-title' and text()='Call Points']"
    )


class HomePageKeyPadsModal(BasePage):
    # Online elements
    online_count = (
        By.XPATH,
        "//div[@data-test='keypad-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-online')]//div[@class='data-card-info-item-value']"
    )
    online_label = (
        By.XPATH,
        "//div[@data-test='keypad-dashboard-body']//span[text()='Online']"
    )

    # Offline elements
    offline_count = (
        By.XPATH,
        "//div[@data-test='keypad-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-offline')]//div[@class='data-card-info-item-value']"
    )
    offline_label = (
        By.XPATH,
        "//div[@data-test='keypad-dashboard-body']//span[text()='Offline']"
    )

    # Offline for more than 30 days elements
    long_offline_count = (
        By.XPATH,
        "//div[@data-test='keypad-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-longOffline')]//div[@class='data-card-info-item-value']"
    )
    long_offline_label = (
        By.XPATH,
        "//div[@data-test='keypad-dashboard-body']//span[text()='Offline for more than 30 days']"
    )

    # Unknown elements
    unknown_count = (
        By.XPATH,
        "//div[@data-test='keypad-dashboard-body']//div[contains(@class, "
        "'data-card-info-item-unknown')]//div[@class='data-card-info-item-value']"
    )
    unknown_label = (
        By.XPATH,
        "//div[@data-test='keypad-dashboard-body']//span[text()='Unknown']"
    )

    keypads_modal_title = (
        By.XPATH,
        "//div[@data-test='keypad-dashboard-body']//span[@class='data-card-title' and text()='Keypads']"
    )


class HeadsetsDetailsPage(BasePage):
    headsets_details_page_title = (
        By.XPATH,
        "//h3[@class='vocovo-devices-header-label' and normalize-space(text()) = 'Headsets']"
    )

    headsets_details_page_count = (
        By.XPATH, "//h3[@class='vocovo-devices-header-label']//span[@class='title-total']"
    )

    # Online elements
    online_count = (
        By.XPATH, "//div[@data-test='vocovo-online-stat-card']//div[@class='count']"
    )
    online_label = (
        By.XPATH, "//div[@data-test='vocovo-online-stat-card']//div[@class='card-title' and text()='Online']"
    )

    # Offline elements
    offline_count = (
        By.XPATH, "//div[@data-test='vocovo-offline-stat-card']//div[@class='count']"
    )
    offline_label = (
        By.XPATH, "//div[@data-test='vocovo-offline-stat-card']//div[@class='card-title' and text()='Offline']"
    )

    # Offline for more than 30 days elements
    long_offline_count = (
        By.XPATH, "//div[@data-test='vocovo-longOffline-stat-card']//div[@class='count']"
    )
    long_offline_label = (
        By.XPATH, "//div[@data-test='vocovo-longOffline-stat-card']//div[@class='card-title' "
                  "and text()='Offline for more than 30 days']"
    )

    # Unknown elements
    unknown_count = (
        By.XPATH, "//div[@data-test='vocovo-unknown-stat-card']//div[@class='count']"
    )
    unknown_label = (
        By.XPATH, "//div[@data-test='vocovo-unknown-stat-card']//div[@class='card-title' and text()='Unknown']"
    )

    # Removed elements
    removed_count = (
        By.XPATH, "//div[@data-test='vocovo-removed-stat-card']//div[@class='count']"
    )
    removed_label = (
        By.XPATH, "//div[@data-test='vocovo-removed-stat-card']//div[@class='card-title' "
                  "and text()='Removed (excluded from total)']"
    )


class HandsetsDetailsPage(BasePage):
    # Handsets title and count
    handsets_details_page_title = (
        By.XPATH, "//h3[@class='vocovo-devices-header-label' and contains(text(), 'Handsets')]"
    )
    handsets_details_page_count = (
        By.XPATH, "//h3[@class='vocovo-devices-header-label']//span[@class='title-total']"
    )

    # Online elements
    online_count = (
        By.XPATH, "//div[@data-test='vocovo-online-stat-card']//div[@class='count']"
    )
    online_label = (
        By.XPATH, "//div[@data-test='vocovo-online-stat-card']//div[@class='card-title' and text()='Online']"
    )

    # Offline elements
    offline_count = (
        By.XPATH, "//div[@data-test='vocovo-offline-stat-card']//div[@class='count']"
    )
    offline_label = (
        By.XPATH, "//div[@data-test='vocovo-offline-stat-card']//div[@class='card-title' and text()='Offline']"
    )

    # Offline for more than 30 days elements
    long_offline_count = (
        By.XPATH, "//div[@data-test='vocovo-longOffline-stat-card']//div[@class='count']"
    )
    long_offline_label = (
        By.XPATH,
        "//div[@data-test='vocovo-longOffline-stat-card']//div[@class='card-title' and text()='Offline for more than 30 days']"
    )

    # Unknown elements
    unknown_count = (
        By.XPATH, "//div[@data-test='vocovo-unknown-stat-card']//div[@class='count']"
    )
    unknown_label = (
        By.XPATH, "//div[@data-test='vocovo-unknown-stat-card']//div[@class='card-title' and text()='Unknown']"
    )

    # Removed elements
    removed_count = (
        By.XPATH, "//div[@data-test='vocovo-removed-stat-card']//div[@class='count']"
    )
    removed_label = (
        By.XPATH,
        "//div[@data-test='vocovo-removed-stat-card']//div[@class='card-title' and text()='Removed (excluded from total)']"
    )


class CallPointsDetailsPage(BasePage):
    # Callpoints title and count
    callpoints_details_page_title = (
        By.XPATH, "//h3[@class='vocovo-devices-header-label' and contains(text(), 'Call Points')]"
    )
    callpoints_details_page_count = (
        By.XPATH, "//h3[@class='vocovo-devices-header-label']//span[@class='title-total']"
    )

    # Online elements
    online_count = (
        By.XPATH, "//div[@data-test='vocovo-online-stat-card']//div[@class='count']"
    )
    online_label = (
        By.XPATH, "//div[@data-test='vocovo-online-stat-card']//div[@class='card-title' and text()='Online']"
    )

    # Offline elements
    offline_count = (
        By.XPATH, "//div[@data-test='vocovo-offline-stat-card']//div[@class='count']"
    )
    offline_label = (
        By.XPATH, "//div[@data-test='vocovo-offline-stat-card']//div[@class='card-title' and text()='Offline']"
    )

    # Offline for more than 30 days elements
    long_offline_count = [(By.XPATH, "//div[@data-test='vocovo-longOffline-stat-card']//div[@class='count']"),
                          (By.XPATH, "//div[contains(@class, 'vocovo-stat-card longOffline')]//div[@class='count']")]

    long_offline_label = (
        By.XPATH, "//div[@data-test='vocovo-longOffline-stat-card']"
                  "//div[@class='card-title' and text()='Offline for more than 30 days']"
    )

    # Unknown elements
    unknown_count = (
        By.XPATH, "//div[@data-test='vocovo-unknown-stat-card']//div[@class='count']"
    )
    unknown_label = (
        By.XPATH, "//div[@data-test='vocovo-unknown-stat-card']//div[@class='card-title' and text()='Unknown']"
    )

    # Removed elements
    removed_count = (
        By.XPATH, "//div[@data-test='vocovo-removed-stat-card']//div[@class='count']"
    )
    removed_label = (
        By.XPATH, "//div[@data-test='vocovo-removed-stat-card']//div[@class='card-title' and text()='Removed (excluded from total)']"
    )


class KeypadsDetailsPage(BasePage):
    # Keypads title and count
    keypads_details_page_title = (
        By.XPATH, "//h3[@class='vocovo-devices-header-label' and contains(normalize-space(text()), 'Keypads')]"
    )
    keypads_details_page_count = (
        By.XPATH, "//h3[@class='vocovo-devices-header-label']//span[@class='title-total']"
    )

    # Online elements
    online_count = (
        By.XPATH, "//div[@data-test='vocovo-online-stat-card']//div[@class='count']"
    )
    online_label = (
        By.XPATH, "//div[@data-test='vocovo-online-stat-card']//div[@class='card-title' and text()='Online']"
    )

    # Offline elements
    offline_count = (
        By.XPATH, "//div[@data-test='vocovo-offline-stat-card']//div[@class='count']"
    )
    offline_label = (
        By.XPATH, "//div[@data-test='vocovo-offline-stat-card']//div[@class='card-title' and text()='Offline']"
    )

    # Offline for more than 30 days elements
    long_offline_count = (
        By.XPATH, "//div[@data-test='vocovo-longOffline-stat-card']//div[@class='count']"
    )
    long_offline_label = (
        By.XPATH, "//div[@data-test='vocovo-longOffline-stat-card']//div[@class='card-title' and text()='Offline for more than 30 days']"
    )

    # Unknown elements
    unknown_count = [
        (By.XPATH, "//div[@data-test='vocovo-unknown-stat-card']//div[@class='count']"),
        (By.XPATH, "//div[@class='vocovo-stat-card unknown']//div[@class='count']")
    ]

    unknown_label = (
        By.XPATH, "//div[@data-test='vocovo-unknown-stat-card']//div[@class='card-title' and text()='Unknown']"
    )

    # Removed elements
    removed_count = (
        By.XPATH, "//div[@data-test='vocovo-removed-stat-card']//div[@class='count']"
    )
    removed_label = (
        By.XPATH, "//div[@data-test='vocovo-removed-stat-card']//div[@class='card-title' and text()='Removed (excluded from total)']"
    )
