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
    login_email = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    login_password = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    login_button = (By.CSS_SELECTOR, "button[data-qa = 'login-button']")
    LOGGED_IN_USER = (By.XPATH, "//a[contains(., 'Logged in as')]")
    logout_button = (By.XPATH, "//a[contains(text(),'Logout')]")

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

    def enter_login_email(self, email):
        self.type(self.login_email, email)

    def enter_login_password(self, password):
        self.type(self.login_password, password)

    def click_login_button(self):
        self.click(self.login_button)

    def is_logged_in(self):
        return self.is_displayed(self.LOGGED_IN_USER)

    def click_logout(self):
        self.click(self.logout_button)
