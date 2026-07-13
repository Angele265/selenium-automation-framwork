from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def get_type(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def select_by_visible_text(self, locator, text):
        dropdown = Select(self.wait.until(EC.visibility_of_element_located(locator)))
        dropdown.select_by_visible_text(text)
