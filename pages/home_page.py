class HomePage:

    URL = "https://automationexercise.com"
    def __init__(self, driver):
        self.driver = driver
    def open(self):
        self.driver.get(self.URL)
    def get_title(self):
        return self.driver.title