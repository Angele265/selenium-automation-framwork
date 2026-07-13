from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from utilities.data_generator import DataGenerator


def test_register(driver):
    home_page = HomePage(driver)
    signup_login_page = SignupLoginPage(driver)

    home_page.open()

    signup_login_page.click_signup_login()

    assert signup_login_page.is_signup_heading_displayed()

    signup_login_page.enter_name(DataGenerator.generate_name())
    signup_login_page.enter_email(DataGenerator.generate_email())

    signup_login_page.click_signup_button()
