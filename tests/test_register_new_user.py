from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from utilities.data_generator import DataGenerator
from pages.account_information_page import AccountInformationPage


def test_register_new_user(driver):
    home_page = HomePage(driver)
    signup_login_page = SignupLoginPage(driver)
    account_page = AccountInformationPage(driver)

    home_page.open()

    signup_login_page.click_signup_login()

    assert signup_login_page.is_signup_heading_displayed()

    signup_login_page.enter_name(DataGenerator.generate_name())
    signup_login_page.enter_email(DataGenerator.generate_email())
    signup_login_page.click_signup_button()

    account_page.select_title_mrs()
    account_page.enter_password("password123456789")
    account_page.select_day("15")
    account_page.select_month("May")
    account_page.select_year("2000")

    account_page.enter_first_name("John")
    account_page.enter_last_name("Nge")
    account_page.enter_address("123 Main Street")
    account_page.select_country("Canada")
    account_page.enter_state("Manching")
    account_page.enter_city("Toronto")
    account_page.enter_zipcode("85077")
    account_page.enter_mobile_number("123456780")

    account_page.click_create_account()

    assert account_page.is_account_created_displayed()

    account_page.click_continue()
