from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.wait_utils import WaitUtils
from pages.base_page import BasePage


class SignupLoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    signup_login_button = (By.LINK_TEXT, "Signup / Login")
    signup_heading = (By.XPATH, "//h2[text()='New User Signup!']")
    name_field = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    email_field = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    signup_button = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    consent_button = (By.XPATH, "//button[contains(., 'Consent') or contains(., 'Accept')]")

    def click_signup_login(self):

        try:
            self.click(self.consent_button)
        except:
            pass

        self.click(self.signup_login_button)

    def is_signup_heading_displayed(self):
        return self.is_displayed(self.signup_heading)

    def enter_name(self, name):
        self.type(self.name_field, name)

    def enter_email(self, email):
        self.type(self.email_field, email)

    def click_signup_button(self):

        self.click(self.signup_button)
