import threading

from main_files.decorator.decorator_func import log_decorator
from pages.auth.auth import Auth
from roles.admin.admin import Admin


@log_decorator
def auth_menu():
    text = '''
1. Login 
2. Logout
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: "))
        if user_input == 1:
            result_login = auth.login()
            if not result_login['is_login']:
                print('Login failed')
                auth_menu()
            elif result_login['role'] == 'admin':
                print("\n<- Welcome Admin ->\n")
                admin_menu()
            elif result_login['role'] == 'employees':
                pass
            elif result_login['role'] == 'companies':
                company_menu()
        elif user_input == 2:
            auth.logout()
            print("Logged out")
            return
        else:
            print("Wrong input")
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


@log_decorator
def admin_menu():
    text = '''
1. Create company
2. Show all companies
3. Logout
    '''
    print(text)
    try:
        admin = Admin()
        admin_input: int = int(input("Choose menu: "))
        if admin_input == 1:
            admin.create_new_company()
            admin_menu()
        elif admin_input == 2:
            admin.show_all_companies()
            admin_menu()
        elif admin_input == 3:
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()


@log_decorator
def company_menu():
    text = '''
1. Manage departments
2. Manage employees
3. Show statistics
4. Logout
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: "))
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            print("Logout")
            threading.Thread(target=auth.logout).start()
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()


@log_decorator
def department_menu_for_company():
    text = '''
1. Create department
2. Update department
3. Delete department
4. Show department
5. Logout
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: "))
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        elif user_input == 5:
            company_menu()
    except Exception as e:
        print(f'Error: {e}')
        department_menu_for_company()


@log_decorator
def employee_menu_for_company():
    pass


if __name__ == '__main__':
    auth = Auth()
    auth.logout()
    auth_menu()
