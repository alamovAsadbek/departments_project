from main_files.decorator.decorator_func import log_decorator
from pages.auth.auth import Auth


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
                pass
            elif result_login['role'] == 'employees':
                pass
            elif result_login['role'] == 'companies':
                pass
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


if __name__ == '__main__':
    auth = Auth()
    auth.logout()
    auth_menu()
