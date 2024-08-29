import threading

from main_files.database.db_setting import get_active, execute_query
from main_files.decorator.decorator_func import log_decorator


class Department:
    @log_decorator
    def create_department(self):
        active_company = threading.Thread(target=get_active, args=('companies',)).start()
        name: str = input("Enter Department Name: ").strip()
        query = '''
        INSERT INTO departments(COMPANY_ID, NAME) VALUES(%s, %s)
        '''
        print(active_company)
        params = (active_company['id'], name,)
        threading.Thread(target=execute_query, args=(query, params)).start()
        print('Department has been created')
        return True
