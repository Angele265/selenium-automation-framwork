from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage

def test_logout_user(driver, user):
    home_page = HomePage(driver)
    login_user = SignupLoginPage(driver)

    home_page.open()

    login_user.click_signup_login()
    login_user.enter_login_email(user.user_email)
    login_user.enter_login_password(user.user_password)
    login_user.click_login_button()
    login_user.click_logout()
    assert login_user.is_signup_heading_displayed()