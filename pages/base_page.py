from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from config.config import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )


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

    def upload_file(self, locator, file_path):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(file_path)

    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def get_product_count(self, locator):
        products = self.wait.until(EC.visibility_of_all_elements_located(locator))
        print(len(products))
        return len(products)


