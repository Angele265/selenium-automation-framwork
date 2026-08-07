from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from config.config import Config


def test_login(driver, user):
    home_page = HomePage(driver)
    signup_page = SignupLoginPage(driver)
    home_page.open()
    assert "Automation Exercise" in home_page.get_title()
    signup_page.click_signup_login()
    assert signup_page.is_signup_heading_displayed()
    signup_page.enter_login_email(user.user_email)
    signup_page.enter_login_password(user.user_password)
    signup_page.click_login_button()
    assert signup_page.is_logged_in()
    signup_page.click_logout()