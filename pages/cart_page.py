from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    product_row = (By.CSS_SELECTOR, "#cart_info_table tbody tr")
    product_name = (By.CSS_SELECTOR, "td.cart_description h4 a[href='/product_details/1']")
    product_price = (By.CSS_SELECTOR, ".cart_price p")
    product_qtty = (By.CSS_SELECTOR, ".cart_quantity button")
    product_total = (By.CSS_SELECTOR, ".cart_total_price")
    remove_product = (By.CSS_SELECTOR, ".cart_quantity_delete")

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

    def remove_product_from_cart(self):
        self.click(self.remove_product)

    def is_product_removed(self):
        return self.wait_until_not_visible(self.product_row)