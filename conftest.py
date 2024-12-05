import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from testrail import TestRailClient
from locators import LoginPage
from dotenv import load_dotenv
from qase_client import QaseClient

load_dotenv()


@pytest.fixture(scope="session")
def run_id(request):
    """Fixture to create a test run and provide run_id."""
    qase_client = QaseClient()

    # Collect test case IDs dynamically from markers
    case_ids = []
    marker_name = None

    for item in request.session.items:
        if "portaluksmoketests" in item.keywords:
            case_ids.extend(get_test_case_ids(item))  # Collect the case IDs from the markers
            marker_name = "Portal UK Smoke Tests Run"  # Name the run dynamically
        # Add more marker checks as needed
        elif "portalussmoketests" in item.keywords:
            case_ids.extend(get_test_case_ids(item))
            marker_name = "Portal US Smoke Tests Run"

    # If no test case IDs are found, exit
    if not case_ids:
        pytest.exit("No test cases found to run.")

    # Create test run dynamically
    run_id = qase_client.create_test_run(marker_name, case_ids)
    if run_id:
        return run_id
    else:
        pytest.exit("Test run creation failed.")


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(items):
    case_ids = []
    marker_name = None

    # Loop through all collected test items and check for markers
    for item in items:
        # Check for the 'portaluksmoketests' marker
        if "portaluksmoketests" in item.keywords:
            case_ids.extend(get_test_case_ids(item))  # Collect the case IDs from the markers
            marker_name = "Portal UK Smoke Tests Run"  # Name the run dynamically

        # Check for other markers and name the test run accordingly
        elif "portalussmoketests" in item.keywords:
            case_ids.extend(get_test_case_ids(item))
            marker_name = "Portal US Smoke Tests Run"

        elif "other_marker2" in item.keywords:
            case_ids.extend(get_test_case_ids(item))
            marker_name = "Portal Link Smoke Tests Run"

    # Ensure we only create the test run once (already handled in the run_id fixture)
    if case_ids and marker_name:
        # Avoid creating a second test run here.
        pass


def get_test_case_ids(item):
    """Extract the numerical test case ID from the marker."""
    case_ids = []
    for marker in item.iter_markers(name="testcaseid"):
        case_id = marker.args[0]  # Extract test case ID like 'PST-1'
        case_number = int(case_id.split("-")[1])  # Extract the numerical part (e.g., 1 for PST-1)
        case_ids.append(case_number)
    return case_ids


@pytest.fixture
def driver():
    is_headless = os.getenv("HEADLESS", "False").lower() == "true"
    chrome_options = Options()

    # Set headless mode if needed
    if is_headless:
        chrome_options.add_argument("--headless")
    else:
        chrome_options.add_argument("--window-size=1920,1080")

    # Use ChromeDriverManager to automatically manage the chromedriver version
    service = Service(ChromeDriverManager().install())

    # Create the WebDriver instance with options and service
    browser = webdriver.Chrome(service=service, options=chrome_options)

    browser.maximize_window()
    yield browser

    browser.quit()


@pytest.fixture
def driver_uk_prod_login_admin(driver):
    base_url = os.getenv("PROD_UK_BASE_URL")
    driver.get(base_url)
    login_page = LoginPage(driver=driver)
    login_page.input_email_field.click()
    login_page.input_email_field.input_text(os.getenv("ADMIN_USERNAME"))
    login_page.input_password_field.click()
    login_page.input_password_field.input_text(os.getenv("ADMIN_PASSWORD"))
    login_page.login_button.click()

    return driver


@pytest.fixture(scope="session")
def testrail_client():
    client = TestRailClient()
    print("TestRail client created")
    return client


@pytest.fixture(scope="session")
def test_run_id(request, testrail_client):
    suite_id = 812  # Example suite ID
    marker = request.config.getoption("--marker")
    case_ids = []

    if marker:
        case_ids = [item.args[0] for item in request.session.items if item.get_closest_marker(marker)]
    else:
        response = testrail_client.client.cases.get_cases(testrail_client.project_id, suite_id=suite_id)
        cases = response.get("cases", [])
        case_ids = [case["id"] for case in cases]

    run_id = testrail_client.create_test_run("Automated Test Run", case_ids, suite_id)
    request.session.config._testrail_client = testrail_client
    request.session.config._test_run_id = run_id
    yield run_id


def pytest_addoption(parser):
    parser.addoption("--marker", action="store", default=None, help="Specify marker to filter tests")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    marker = item.get_closest_marker("testrail")
    if marker is not None:
        case_id = marker.args[0]
        status_id = 1 if report.outcome == "passed" else 5
        comment = report.longreprtext if report.failed else ""
        testrail_client = item.session.config._testrail_client
        test_run_id = item.session.config._test_run_id
        testrail_client.update_test_result(test_run_id, case_id, status_id, comment)


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    session.config._testrail_client = None
    session.config._test_run_id = None


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    if session.config._testrail_client and session.config._test_run_id:
        session.config._testrail_client.close_test_run(session.config._test_run_id)


"""The below is a check email fixture for gmail which we can implement in case we need checking email content"""

# import imaplib
# import email
# from email.header import decode_header

# @pytest.fixture
# def check_email():
#     def _check_email(subject_to_look_for, search_in_body=None):
#         try:
#             username = os.getenv("GMAIL_USERNAME")
#             password = os.getenv("GMAIL_APP_PASSWORD")
#
#             # Connect to Gmail IMAP server
#             mail = imaplib.IMAP4_SSL("imap.gmail.com")
#             mail.login(username, password)
#             mail.select("inbox")
#
#             # Search for emails with the specified subject
#             status, messages = mail.search(None, 'SUBJECT', f'"{subject_to_look_for}"')
#             email_ids = messages[0].split()
#
#             if email_ids:
#                 for email_id in email_ids:
#                     status, msg_data = mail.fetch(email_id, "(RFC822)")
#                     for response_part in msg_data:
#                         if isinstance(response_part, tuple):
#                             msg = email.message_from_bytes(response_part[1])
#                             subject, encoding = decode_header(msg["Subject"])[0]
#                             if isinstance(subject, bytes):
#                                 subject = subject.decode(encoding or "utf-8")
#
#                             if subject_to_look_for in subject:
#                                 if msg.is_multipart():
#                                     for part in msg.walk():
#                                         content_type = part.get_content_type()
#                                         content_disposition = str(part.get("Content-Disposition"))
#
#                                         if "attachment" not in content_disposition and content_type == "text/plain":
#                                             body = part.get_payload(decode=True).decode()
#
#                                             # Check if a specific text (e.g., link, code) exists in the email body
#                                             if search_in_body and search_in_body in body:
#                                                 return True, body
#
#                                             return True, body
#                                 else:
#                                     body = msg.get_payload(decode=True).decode()
#
#                                     # Check if a specific text (e.g., link, code) exists in the email body
#                                     if search_in_body and search_in_body in body:
#                                         return True, body
#
#                                     return True, body
#             else:
#                 return False, "No email found with the specified subject."
#
#             mail.logout()
#
#         except Exception as e:
#             return False, f"An error occurred: {str(e)}"
#
#     return _check_email