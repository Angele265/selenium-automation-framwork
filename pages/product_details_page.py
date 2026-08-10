from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductDetailsPage(BasePage):
    product_detail_button = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    product_name = (By.XPATH, "//h2[normalize-space()='Blue Top']")
    category = (By.XPATH, "//p[normalize-space()='Category: Women > Tops']")
    price = (By.XPATH, "//div[@class='product-information']//span/span")
    availability = (By.XPATH, "//p[.//b[normalize-space()='Availability:']]")
    condition = (By.XPATH, "//p[.//b[normalize-space()='Condition:']]")
    brand = (By.XPATH, "//p[.//b[normalize-space()='Brand:']]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_product_details(self):
        self.click(self.product_detail_button)

    def get_product_name(self):
        return self.get_type(self.product_name)

    def get_category(self):
        return self.get_type(self.category)

    def get_price(self):
        return self.get_type(self.price)

    def get_availability(self):
        return self.get_type(self.availability)

    def get_condition(self):
        return self.get_type(self.condition)

    def get_brand(self):
        return self.get_type(self.brand)