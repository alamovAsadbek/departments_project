import string
from random import random

from main_files.decorator.decorator_func import log_decorator


class Admin:
    @log_decorator
    def generate_username(self, name: str) -> str:
        """
        Generates a random username based on the provided name.

        Parameters:
            name (str): The base name to use for the username.

        Returns:
            str: A randomly generated username.
        """
        # Strip any leading/trailing whitespace and convert name to lowercase
        base_name = name.strip().lower()

        # Generate a random number between 1000 and 9999
        random_number = random.randint(1000, 9999)

        # Generate a random string of 2 letters
        random_letters = ''.join(random.choices(string.ascii_lowercase, k=2))

        # Combine the base name with the random number and letters
        username = f"{base_name}{random_number}{random_letters}"

        return username

    @log_decorator
    def create_new_company(self):
        company_name = input("Enter company name: ").strip()
        while True:
            username = self.generate_username(company_name)
            query='''
            SELECT * FROM 
            '''
