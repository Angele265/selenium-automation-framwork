from utilities.wait_utils import WaitUtils
class AccountInformationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)