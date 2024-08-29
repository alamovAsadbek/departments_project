import threading

from psycopg2 import sql

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
        USERNAME VARCHAR(60) NOT NULL UNIQUE,
        PASSWORD VARCHAR(256) NOT NULL,
        COMPANY_ID BIGINT REFERENCES companies(ID) NOT NULL,
        DEPARTMENT BIGINT REFERENCES departments(ID) NOT NULL,
        CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        IS_LOGIN BOOLEAN DEFAULT FALSE
        );
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_department_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS departments (
        ID BIGSERIAL PRIMARY KEY,
        NAME VARCHAR(60) NOT NULL,
        COMPANY_ID BIGINT REFERENCES companies(ID) NOT NULL,
        CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_company_table(self):
        try:
            query = '''
                    CREATE TABLE IF NOT EXISTS companies (
                    ID BIGSERIAL PRIMARY KEY,
                    NAME VARCHAR(60) NOT NULL,
                    USERNAME VARCHAR(60) NOT NULL UNIQUE,
                    PASSWORD  VARCHAR(256) NOT NULL,
                    IS_LOGIN BOOLEAN DEFAULT FALSE,
                    CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                    );
                    '''
            execute_query(query)
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def login(self):
        tables = ['employees', 'companies']
        username = input('Username or email: ').strip().lower()
        password = input("Password: ").strip()
        if username == self.__admin_username and password == self.__admin_password:
            return {'is_login': True, 'role': 'admin'}
        print('Checked...')
        for table in tables:
            query = sql.SQL('SELECT * FROM {} WHERE USERNAME=%s AND PASSWORD=%s;').format(
                sql.Identifier(table)
            )
            params = (username, password)
            result = execute_query(query, params, fetch='one')
            if result is not None:
                query = sql.SQL('UPDATE {} SET IS_LOGIN=TRUE WHERE ID=%s;').format(
                    sql.Identifier(table)
                )
                params = (f'{result["id"]}',)
                print(result, result['id'])
                threading.Thread(target=execute_query, args=(query, params)).start()
                return {'is_login': True, 'role': table}
        return {'is_login': False}

    @log_decorator
    def logout(self):
        print('Waiting...')
        self.create_company_table()
        self.create_department_table()
        self.create_employee_table()
        tables = ['employees', 'companies']
        for table in tables:
            query = sql.SQL('UPDATE {} SET IS_LOGIN=FALSE;').format(
                sql.Identifier(table)
            )
            threading.Thread(target=execute_query, args=(query,)).start()
        return True

    '''
    Programma sekin ishga tushadi. Chunki birinchi tablelarni yaratib oladi yani keyinchalik xato chiqmasligi uchun.
    Thread bilan qilsam bulardi lekin bu ko'plab xatoliklarga olib keladi yani thread bn yozganimda database remote 
    bulgani uchun yaratishga qanchadir vaqt sarflaydi va u hali yaratmasdan turib meni is_loginni false qilishga 
    urinayotgan bulaman usha uchun xatolik kelib chiqmasligi uchun threadga yozmadim
    '''
