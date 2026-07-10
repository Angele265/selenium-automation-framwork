import pytest

from utilities.driver_factory import DriverFactory

@pytest.fixture
def driver():
    driver = DriverFactory.get_chrome_driver()

    yield driver

    driver.quit()