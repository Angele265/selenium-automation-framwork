import pytest
import os
from datetime import datetime
from utilities.driver_factory import DriverFactory
from utilities.data_generator import DataGenerator

@pytest.fixture
def driver():
    driver = DriverFactory.get_chrome_driver()

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            filename = f"{item.name}_{timestamp}.png"

            filepath = os.path.join("screenshots", filename)

            driver.save_screenshot(filepath)

            print(f"\nScreenshot saved: {filepath}")

@pytest.fixture
def user():
    test_user = DataGenerator.generate_user_info()
    return test_user