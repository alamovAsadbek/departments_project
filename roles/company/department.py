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
    def show_department(self):
        pass
