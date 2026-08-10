from pages.home_page import HomePage
from pages.contact_us_page import ContactUs

def test_contact_us(driver, user):
    home_page = HomePage(driver)
    contact_us = ContactUs(driver)


    home_page.open()

    contact_us.click_contact_us_button()
    contact_us.enter_user(user.first_name)
    contact_us.enter_email(user.user_email)
    contact_us.enter_subject(user.subject)
    contact_us.enter_message(user.message)
    contact_us.send_file(user.file_path)
    contact_us.click_submit()
    contact_us.click_accept_alert()
    assert contact_us.is_success_message_displayed()
