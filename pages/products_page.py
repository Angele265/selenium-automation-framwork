from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductSearch(BasePage):

    products_button = (By.CSS_SELECTOR, "a[href='/products']")
    search_product_field = (By.ID, "search_product")
    search_button = (By.ID, "submit_search")
    products = (By.CSS_SELECTOR, "div.productinfo.text-center")
    add_to_cart = (By.CSS_SELECTOR, "a[data-product-id='1'].add-to-cart")

    def __init__(self, driver):
        super().__init__(driver)

    def click_products_button(self):
        self.click(self.products_button)

    def search_products(self, search_item):
        self.type(self.search_product_field, search_item)

    def submit_search(self):
        self.click(self.search_button)

    def are_products_displayed(self):
        return self.get_product_count(self.products) > 0

    def total_product(self):
        return self.get_product_count(self.products)

    def add_item_to_cart(self):
        self.click(self.add_to_cart)
