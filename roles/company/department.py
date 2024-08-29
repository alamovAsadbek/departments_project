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
        print(self.__active_company, self.__active_company['id'])
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
