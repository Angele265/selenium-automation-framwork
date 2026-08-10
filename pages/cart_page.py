from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    product_row = (By.CSS_SELECTOR, "#cart_info_table tbody tr")
    product_name = (By.CSS_SELECTOR, ".cart_description h4 a")
    product_price = (By.CSS_SELECTOR, ".cart_price p")
    product_qtty = (By.CSS_SELECTOR, ".cart_quantity button")
    product_total = (By.CSS_SELECTOR, ".cart_total_price")

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_name(self):
        return self.get_type(self.product_name)

    def get_product_price(self):
        return self.get_type(self.product_price)

    def get_product_qtty(self):
        return self.get_type(self.product_qtty)

    def get_product_total(self):
        return self.get_type(self.product_total)

    def is_product_in_cart(self):
        return self.is_displayed(self.product_name)