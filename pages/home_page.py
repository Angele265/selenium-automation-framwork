from config.config import Config
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class HomePage(BasePage):
    cart = (By.XPATH, "//a[contains(@href,'view_cart')]")


    def __init__(self, driver):
        super().__init__(driver)
    def open(self):
        self.driver.get(Config.BASE_URL )
    def get_title(self):
        return self.driver.title

    def click_cart(self):
        self.click(self.cart)