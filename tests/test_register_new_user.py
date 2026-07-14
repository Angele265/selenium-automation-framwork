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

    user = DataGenerator.generate_user_info()
    signup_login_page.enter_name(user.name)
    signup_login_page.enter_email(user.email)
    signup_login_page.click_signup_button()

    account_page.select_title_mrs()
    account_page.enter_password(user.password)
    account_page.select_day(user.day)
    account_page.select_month(user.month)
    account_page.select_year(user.year)

    account_page.enter_first_name(user.first_name)
    account_page.enter_last_name(user.last_name)
    account_page.enter_address(user.address)
    account_page.select_country(user.country)
    account_page.enter_state(user.state)
    account_page.enter_city(user.city)
    account_page.enter_zipcode(user.zipcode)
    account_page.enter_mobile_number(user.mobile_number)

    account_page.click_create_account()

    assert account_page.is_account_created_displayed()

    account_page.click_continue()
