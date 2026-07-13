from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.wait_utils import WaitUtils


class SignupLoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    # Locators
    signup_login_button = (By.LINK_TEXT, "Signup / Login")
    signup_heading = (By.XPATH, "//h2[text()='New User Signup!']")
    name_field = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    email_field = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    signup_button = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    def click_signup_login(self):

        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Consent') or contains(., 'Accept')]"))
            ).click()
        except:
            pass

        self.wait.wait_for_clickable(self.signup_login_button).click()

    def is_signup_heading_displayed(self):
        return self.wait.wait_for_visibility(self.signup_heading).is_displayed()

    def enter_name(self, name):
        self.wait.wait_for_visibility(self.name_field).send_keys(name)


    def enter_email(self, email):
        self.wait.wait_for_visibility(self.email_field).send_keys(email)

    def click_signup_button(self):

        self.wait.wait_for_clickable(self.signup_button).click()
