import threading

from main_files.database.db_setting import get_active, execute_query
from main_files.decorator.decorator_func import log_decorator


class Department:
    def __init__(self):
        self.__active_company = get_active('companies')

    @log_decorator
    def create_department(self):
        print("Waiting...")
        name: str = input("Enter Department Name: ").strip()
        query = '''
        INSERT INTO departments(COMPANY_ID, NAME) VALUES(%s, %s)
        '''
        params = (self.__active_company['id'], name,)
        threading.Thread(target=execute_query, args=(query, params)).start()
        print(f'{name} has been created')
        return True

    @log_decorator
    def get_department(self):
        query = '''
                SELECT * FROM departments WHERE COMPANY_ID=%s;
        '''
        params = (self.__active_company['id'],)
        return execute_query(query, params, fetch='all')

    @log_decorator
    def show_department(self):
        print('Waiting...')
        count = 1
        result_get = self.get_department()
        if result_get is None:
            print("Data is not found")
            return False
        for department in result_get:
            print(f'<- \t{count} \t->\n')
            print(f"ID: {department['id']}\nName: {department['name']}\nCreated: {department['created_at']}\n")
            count += 1
        if count == 1:
            print("Department has been found")
            return False
        return True

    @log_decorator
    def update_department(self):
        if not self.show_department():
            return False
        department_id = int(input("Enter Department ID: ").strip())
        print("Waiting...")
        query = '''
        SELECT * FROM departments WHERE COMPANY_ID=%s and ID=%s;
        '''
        params = (self.__active_company['id'], department_id)
        get_department = execute_query(query, params, fetch='one')
        if get_department is None:
            print("Data is not found")
            return False
        name = input("Enter Department New Name: ").strip()
        query = '''
        UPDATE departments SET NAME=%s WHERE ID=%s;
        '''
        params = (name, department_id)
        threading.Thread(target=execute_query, args=(query, params)).start()
        print(f'{name} has been updated')
        return True
