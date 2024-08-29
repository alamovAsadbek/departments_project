import string
import threading
from random import random

from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class Admin:
    @log_decorator
    def generate_username(self, name: str) -> str:
        base_name = name.strip().lower()
        random_number = random.randint(1000, 9999)
        random_letters = ''.join(random.choices(string.ascii_lowercase, k=2))
        return f"{base_name}{random_number}{random_letters}"

    @log_decorator
    def generate_password(self, length: int = 12) -> str:
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(characters, k=length))

    @log_decorator
    def create_new_company(self):
        company_name = input("Enter company name: ").strip()
        while True:
            print(f"{company_name} company profile is being created")
            username = self.generate_username(company_name)
            query = '''
            SELECT * FROM %s WHERE USERNAME=%s
            '''
            params = ('companies', username)
            get_data = execute_query(query, params, fetch='one')
            if get_data is not None:
                continue
            password = self.generate_password(length=4)
            print(f"\nCompany name is {company_name}\nCompany username is {username}\nPassword is {password}")
            query = '''
            INSERT INTO companies (NAME, USERNAME, PASSWORD) VALUES (%s, %s, %s)
            '''
            params = (company_name, username, password)
            threading.Thread(target=execute_query, args=(query, params)).start()
            print(f"\n{company_name} company created successfully")
            return True
