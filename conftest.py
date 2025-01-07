import os
import pytest
import time
from functools import wraps
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from qase_client import QaseClient
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from locators import LoginPage  # Ensure this is properly included

load_dotenv()


def sanitize_count(count_text):
    count_text = count_text.strip()
    if count_text == "-":
        return 0
    return int(count_text)


# Qase Test Decorator
def qase_test(case_id):
    """Decorator to handle Qase test result reporting."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            qase_client = QaseClient()
            run_id = kwargs.get('run_id')
            start_time = time.time()
            failure_reason = None

            try:
                func(*args, **kwargs)  # Execute the test
                elapsed_time = time.time() - start_time
                qase_client.update_test_result(run_id, case_id, "passed",
                                               comment="Test completed successfully", time=int(elapsed_time))
            except (AssertionError, StaleElementReferenceException, TimeoutException) as e:
                failure_reason = str(e)
                elapsed_time = time.time() - start_time
                qase_client.update_test_result(run_id, case_id, "failed",
                                               comment=f"Test failed. Reason: {failure_reason}", time=int(elapsed_time))
                raise
            except Exception as e:  # Catch-all for unexpected exceptions
                failure_reason = f"Unexpected error: {str(e)}"
                elapsed_time = time.time() - start_time
                qase_client.update_test_result(run_id, case_id, "failed",
                                               comment=f"Test failed. Reason: {failure_reason}", time=int(elapsed_time))
                raise
            finally:
                print(f"Test {'failed' if failure_reason else 'passed'}: {failure_reason or 'No issues'}")
        return wrapper
    return decorator


@pytest.fixture(scope="session")
def run_id(request):
    """Fixture to create a test run in Qase."""
    qase_client = QaseClient()

    # Retrieve case IDs and marker name from config
    case_ids = getattr(request.config, "case_ids", [])
    marker_name = getattr(request.config, "marker_name", "Default Test Run")

    if not case_ids:
        pytest.exit("No test cases found to run.")

    # Create a test run
    run_id = qase_client.create_test_run(marker_name, case_ids)
    if run_id:
        return run_id
    else:
        pytest.exit("Failed to create test run in Qase.")


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(config, items):
    """Hook to dynamically collect test case IDs and markers."""
    case_ids = []
    marker_name = None

    # Get the selected marker from pytest -m argument
    selected_marker = config.getoption("-m")

    # Iterate through collected items (tests)
    for item in items:
        # Check if the item has the selected marker
        if selected_marker in item.keywords:
            for marker in item.iter_markers():
                if marker.name == "testcaseid":
                    # Extract and store test case IDs
                    case_ids.append(int(marker.args[0].split("-")[1]))
                    marker_name = f"Run for marker: {selected_marker}"

    # Attach case IDs and marker name to the pytest config for later use
    config.case_ids = case_ids
    config.marker_name = marker_name

    # Debugging information
    print(f"Collected Case IDs: {case_ids}")
    print(f"Test Run Marker: {marker_name}")


@pytest.fixture
def driver():
    """Fixture to initialize and return a Selenium WebDriver."""
    is_headless = os.getenv("HEADLESS", "False").lower() == "true"
    chrome_options = Options()

    # Set headless mode if needed
    if is_headless:
        chrome_options.add_argument("--headless")
    else:
        chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)

    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def driver_uk_prod_login_admin(driver):
    """Fixture to log in as an admin user on the UK production site."""
    base_url = os.getenv("PROD_UK_BASE_URL")
    driver.get(base_url)
    login_page = LoginPage(driver=driver)
    login_page.input_email_field.click()
    login_page.input_email_field.input_text(os.getenv("ADMIN_USERNAME"))
    login_page.input_password_field.click()
    login_page.input_password_field.input_text(os.getenv("ADMIN_PASSWORD"))
    login_page.login_button.click()

    return driver
