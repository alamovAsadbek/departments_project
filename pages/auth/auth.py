import threading

from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class Auth:
    def __init__(self):
        self.__admin_username = 'admin'
        self.__admin_password = 'admin'

    @log_decorator
    def create_employee_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS employees (
        ID BIGSERIAL PRIMARY KEY,
        FIRST_NAME VARCHAR(60) NOT NULL,
        LAST_NAME VARCHAR(60) NOT NULL,
        EMAIL VARCHAR(60) NOT NULL UNIQUE,
        PASSWORD VARCHAR(256) NOT NULL,
        COMPANY_ID BIGINT REFERENCES companies(ID) NOT NULL,
        DEPARTMENT BIGINT REFERENCES departments(ID) NOT NULL,
        CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        IS_LOGIN BOOLEAN DEFAULT FALSE,
        )
        '''
        threading.Thread(target=execute_query, args=(query,)).start()
        return True

    @log_decorator
    def create_department_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS departments (
        ID BIGSERIAL PRIMARY KEY,
        NAME VARCHAR(60) NOT NULL,
        COMPANY_ID BIGINT REFERENCES companies(ID) NOT NULL
        )
        '''
        threading.Thread(target=execute_query, args=(query,)).start()
        return True

    @log_decorator
    def create_company_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS companies (
        ID BIGSERIAL PRIMARY KEY,
        NAME VARCHAR(60) NOT NULL,
        USERNAME VARCHAR(60) NOT NULL UNIQUE,
        PASSWORD  VARCHAR(256) NOT NULL,
        IS_LOGIN BOOLEAN DEFAULT FALSE,
        )
        '''
        threading.Thread(target=execute_query, args=(query,)).start()
        return True

    @log_decorator
    def logout(self):
        self.create_company_table()
        self.create_employee_table()
        self.create_department_table()
        query = 'UPDATE %s SET IS_LOGIN=FALSE;'
        threading.Thread(target=execute_query, args=(query, 'employees',)).start()
        threading.Thread(target=execute_query, args=(query, 'departments',)).start()
        threading.Thread(target=execute_query, args=(query, 'companies',)).start()
        return True
