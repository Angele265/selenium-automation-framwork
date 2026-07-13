from utilities.wait_utils import WaitUtils
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountInformationPage(BasePage):
    mr_field = (By.ID, "id_gender1")
    mrs_field = (By.ID, "id_gender2")
    password_field = (By.ID, "password")
    day_field = (By.ID, "days")
    month_field = (By.ID, "months")
    year_field = (By.ID, "years")
    newsletter_field = (By.ID, "newsletter")
    special_offer_field = (By.ID, "optin")
    first_name_field = (By.ID, "first_name")
    last_name_field = (By.ID, "last_name")
    address_field = (By.ID, "address1")
    company_field = (By.ID, "company")
    country_field = (By.ID, "country")
    state_field = (By.ID, "state")
    city_field = (By.ID, "city")
    zipcode_field = (By.ID, "zipcode")
    mobile_number_field = (By.ID, "mobile_number")
    create_account_button = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    account_created_message_field = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    continue_button = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def __init__(self, driver):
        super().__init__(driver)

    def select_title_mrs(self):
        self.click(self.mrs_field)

    def enter_password(self, password):
        self.type(self.password_field, password)

    def select_day(self, day):
        self.select_by_visible_text(self.day_field, day)

    def select_month(self, month):
        self.select_by_visible_text(self.month_field, month)

    def select_year(self, year):
        self.select_by_visible_text(self.year_field, year)

    def enter_first_name(self, first_name):
        self.type(self.first_name_field, first_name)

    def enter_last_name(self, last_name):
        self.type(self.last_name_field, last_name)

    def enter_address(self, address):
        self.type(self.address_field, address)

    def select_country(self, country):
        self.select_by_visible_text(self.country_field, country)

    def enter_state(self, state):
        self.type(self.state_field, state)

    def enter_city(self, city):
        self.type(self.city_field, city)

    def enter_zipcode(self, zipcode):
        self.type(self.zipcode_field, zipcode)

    def enter_mobile_number(self, mobile):
        self.type(self.mobile_number_field, mobile)

    def click_create_account(self):
        self.click(self.create_account_button)

    def is_account_created_displayed(self):
        return self.is_displayed(self.account_created_message_field)

    def click_continue(self):
        self.click(self.continue_button)
