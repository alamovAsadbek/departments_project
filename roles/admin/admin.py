import random
import re
import threading

from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class Admin:
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
    def create_new_company(self):
        company_name = input("Enter company name: ").strip()
        while True:
            print(f"{company_name} company profile is being created")
            username = self.generate_username(company_name)

            # Correct SQL Query
            query = '''
            SELECT * FROM companies WHERE USERNAME=%s
            '''
            params = (username,)
            get_data = execute_query(query, params, fetch='one')
            if get_data is not None:
                continue

            password = self.generate_password()
            print(f"\nCompany name is {company_name}\nCompany username is {username}\nPassword is {password}")

            # Correct SQL Query
            query = '''
            INSERT INTO companies (NAME, USERNAME, PASSWORD) VALUES (%s, %s, %s)
            '''
            params = (company_name, username, password)
            threading.Thread(target=execute_query, args=(query, params)).start()
            print(f"\n{company_name} company created successfully")
            return True

    @log_decorator
    def show_all_companies(self):
        pass
