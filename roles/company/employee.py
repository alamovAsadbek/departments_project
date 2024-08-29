import random
import re
import threading

from main_files.database.db_setting import execute_query, get_active
from main_files.decorator.decorator_func import log_decorator
from roles.company.department import Department


class EmployeeForCompany:
    def __init__(self):
        self.__company = get_active('companies')
        self.__department = Department()

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
            SELECT * FROM employees WHERE username=?s;
            '''
            params = (username,)
            result = execute_query(query, params)
            if result is not None:
                continue
            return username

    @log_decorator
    def get_department(self):
        if not self.__department.show_department():
            return False
        choose_department: int = int(input("Enter department ID: ").strip())
        query = '''
                SELECT * FROM departments WHERE COMPANY_ID=%s and ID=%s;
                '''
        params = (self.__company['id'], choose_department)
        get_department = execute_query(query, params, fetch='one')
        if get_department is None:
            print("Data is not found")
            return False
        return get_department

    @log_decorator
    def create_employee(self):
        first_name: str = input("First Name: ").strip()
        last_name: str = input("Last Name: ").strip()
        arrival_time = input("Enter arrival time (12:00): ").strip()
        leave_time = input("Enter arrival time (12:00): ").strip()
        print("\n Choose department: \n")
        result_department = self.get_department()
        if not result_department:
            print('Something is wrong')
            return False
        username = self.get_username(name=first_name)
        password = self.generate_password()
        query = '''
        INSERT INTO employees (FIRST_NAME, LAST_NAME, USERNAME, PASSWORD, COMPANY_ID, DEPARTMENT_ID, ARRIVAL_TIME, 
        LEAVE_TIME) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''
        params = (first_name, last_name, username, password, self.__company['id'], result_department['id'],
                  arrival_time, leave_time)
        threading.Thread(target=execute_query, args=(query, params,)).start()
        print(f'\nEmployee username: {username}\nEmployee password: {password}\n')
        print("Employee created")
        return True
