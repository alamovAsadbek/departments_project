import random
import re

from main_files.decorator.decorator_func import log_decorator


class EmployeeForCompany:
    @log_decorator
    def generate_username(self, name: str) -> str:
        # Strip and lower case the name
        base_name = name.strip().lower()
        # Replace spaces with underscores
        base_name = base_name.replace(' ', '_')
        # Remove any non-alphanumeric characters except underscores
        base_name = re.sub(r'[^\w]', '', base_name)
        # Generate a random number
        random_number = random.randint(1, 9999)
        return f"{base_name}_{random_number}"

    @log_decorator
    def generate_password(self, ) -> int:
        random_num = random.randint(1000, 9999)
        return random_num

    @log_decorator
    def get_username(self, name: str) -> str:
        pass

    @log_decorator
    def create_employee(self):
        first_name: str = input("First Name: ").strip()
        last_name: str = input("Last Name: ").strip()
