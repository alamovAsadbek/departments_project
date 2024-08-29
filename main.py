from main_files.decorator.decorator_func import log_decorator


@log_decorator
def auth_menu():
    text = '''
1. Login 
2. Logout
    '''
    print(text)
    try:
        pass
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()
