import time


class DataGenerator:
    @staticmethod
    def generate_name():
        return "UserTest"

    @staticmethod
    def generate_email():
        timestamp = int(time.time())
        return f"UserTest{timestamp}@example.com"
