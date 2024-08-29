import random
import re

from main_files.database.db_setting import execute_query, get_active
from main_files.decorator.decorator_func import log_decorator


class EmployeeForCompany:
    def __init__(self):
        self.__company = get_active('companies')

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
        while True:
            username = self.generate_username(name)
            query = '''
            SELECT * FROM employees WHERE username=?s
            '''
            params = (username,)
            result = execute_query(query, params)
            if result is not None:
                continue
            return username

    @log_decorator
    def get_department(self, name: str) -> int:
        pass

    @log_decorator
    def create_employee(self):
        first_name: str = input("First Name: ").strip()
        last_name: str = input("Last Name: ").strip()
