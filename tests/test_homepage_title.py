from pages.home_page import HomePage
from utilities.logger import Logger

def test_home_page_title(driver):

    home_page = HomePage(driver)
    logger = Logger.get_logger()
    home_page.open()
    title = home_page.get_title()
    if "Automation Exercise" in title:
        logger.info(f"Page title verified successfully: {title}")
    else:
        logger.error(f"Expected 'Automation Exercise' but got '{title}'")
        assert False


