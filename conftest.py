import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from testrail import TestRailClient
from locators import LoginPage
from dotenv import load_dotenv


load_dotenv()


@pytest.fixture
def driver():
    is_headless = os.getenv("HEADLESS", "False").lower() == "false"
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
def driver_login_admin(driver):
    base_url = os.getenv("BASE_URL")
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
