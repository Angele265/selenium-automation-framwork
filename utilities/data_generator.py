import time
from models.users import User


class DataGenerator:
    @staticmethod
    def generate_user_info():
        timestamp = int(time.time())
        return User(
            first_name="John",
            last_name="Nge",
            name="John",
            email=f"UserTest{timestamp}@example.com",
            password="password123456789",
            day="15",
            month="May",
            year="2000",
            address="123 Main Street",
            city="Toronto",
            state="Manching",
            country="Canada",
            mobile_number="123456780",
            zipcode="85077"
        )
