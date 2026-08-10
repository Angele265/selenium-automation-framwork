from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactUs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    contact_us_button = (By.CSS_SELECTOR, "a[href='/contact_us']")
    success_message = (By.CSS_SELECTOR, "div.status.alert-success")
    user_name = (By.CSS_SELECTOR, "input[data-qa='name']")
    user_email = (By.CSS_SELECTOR, "input[data-qa='email']")
    subject_field = (By.CSS_SELECTOR, "input[data-qa='subject']")
    message_field = (By.CSS_SELECTOR, "textarea[data-qa='message']")
    submit_button = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    upload_file_field = (By.NAME, "upload_file")

    def click_contact_us_button(self):
        self.click(self.contact_us_button)
    def enter_user(self, name):
        self.type(self.user_name, name)
    def enter_email(self, email):
        self.type(self.user_email, email)
    def enter_subject(self, subject):
        self.type(self.subject_field, subject)
    def enter_message(self, message):
        self.type(self.message_field, message)
    def click_submit(self):
        self.click(self.submit_button)
    def send_file(self,file_path):
        self.upload_file(self.upload_file_field, file_path)
    def click_accept_alert(self):
        self.accept_alert()
    def is_success_message_displayed(self):
        return self.is_displayed(self.success_message)






