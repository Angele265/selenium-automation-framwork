from config.config import Config
from pages.base_page import BasePage
class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    def open(self):
        self.driver.get(Config.BASE_URL )
    def get_title(self):
        return self.driver.title