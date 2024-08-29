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
                print("\n<- Welcome Admin ->\n")
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


@log_decorator
def admin_menu():
    text = '''
1. Manage departments
2. Manage employees | CRUD
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


if __name__ == '__main__':
    auth = Auth()
    auth.logout()
    auth_menu()
    import threading

from main_files.decorator.decorator_func import log_decorator
from pages.auth.auth import Auth


@log_decorator
def auth_menu():
    """
    Displays the authentication menu where users can choose to login or logout.
    """
    text = '''
1. Login 
2. Logout
    '''
    print(text)
    try:
        # Get user input for menu choice
        user_input: int = int(input("Choose menu: "))

        if user_input == 1:
            # Attempt to log in
            result_login = auth.login()

            if not result_login['is_login']:
                print('Login failed')
                # If login failed, show the menu again
                auth_menu()
            elif result_login['role'] == 'admin':
                print("\n<- Welcome Admin ->\n")
                # Add additional admin menu logic here
                pass
            elif result_login['role'] == 'employees':
                # Add employee-specific logic here
                pass
            elif result_login['role'] == 'companies':
                # Add company-specific logic here
                pass

        elif user_input == 2:
            # Log out the current user
            auth.logout()
            print("Logged out")
            return

        else:
            # Handle invalid menu input
            print("Wrong input")
            auth_menu()

    except Exception as e:
        # Handle exceptions and show error message
        print(f'Error: {e}')
        auth_menu()


@log_decorator
def company_menu():
    """
    Displays the admin menu where admins can manage departments, employees, view statistics, or logout.
    """
    text = '''
1. Manage departments
2. Manage employees
3. Show statistics
4. Logout
    '''
    print(text)
    try:
        # Get user input for menu choice
        user_input: int = int(input("Choose menu: "))

        if user_input == 1:
            # Add department management logic here
            department_menu_for_company()
        elif user_input == 2:
            # Add employee management logic here
            employee_menu_for_company()
        elif user_input == 3:
            # Add statistics viewing logic here
            pass
        elif user_input == 4:
            # Logout the current user and show authentication menu
            print("Logout")
            # Run logout in a separate thread
            threading.Thread(target=auth.logout).start()
            auth_menu()

    except Exception as e:
        # Handle exceptions and show error message
        print(f'Error: {e}')
        admin_menu()


@log_decorator
def employee_menu_for_company():
    """
    Displays the employee management menu where users can create, update, delete employees,
    show employees, or log out.
    """
    text = '''
1. Create employee
2. Update employee
3. Delete employee
4. Show employees
5. Logout
    '''
    print(text)
    try:
        # Get user input for menu choice
        user_input: int = int(input("Choose menu: "))

        if user_input == 1:
            # Logic to create a new employee should be added here
            pass
        elif user_input == 2:
            # Logic to update an existing employee should be added here
            pass
        elif user_input == 3:
            # Logic to delete an employee should be added here
            pass
        elif user_input == 4:
            # Logic to display a list of employees should be added here
            pass
        elif user_input == 5:
            # Go back to the admin menu
            admin_menu()

        else:
            # Handle invalid menu input
            print("Wrong input")
            # Show the employee menu again
            employee_menu_for_company()

    except Exception as e:
        # Handle exceptions and show error message
        print(f'Error: {e}')
        # Show the employee menu again
        employee_menu_for_company()


@log_decorator
def department_menu_for_company():
    """
    Displays the department management menu where users can create, update, delete departments,
    view statistics, or log out.
    """
    text = '''
1. Create a new department
2. Update department
3. Delete department
4. Show departments
5. Logout
    '''
    print(text)
    try:
        # Get user input for menu choice
        user_input: int = int(input("Choose menu: "))

        if user_input == 1:
            # Logic to create a new department should be added here
            pass
        elif user_input == 2:
            # Logic to update an existing department should be added here
            pass
        elif user_input == 3:
            # Logic to delete a department should be added here
            pass
        elif user_input == 4:
            # Logic to show department statistics should be added here
            pass
        elif user_input == 5:
            # Go back to the admin menu
            admin_menu()

        else:
            # Handle invalid menu input
            print("Wrong input")
            # Show the department menu again
            department_menu_for_company()

    except Exception as e:
        # Handle exceptions and show error message
        print(f'Error: {e}')
        # Show the department menu again
        department_menu_for_company()


if __name__ == '__main__':
    # Instantiate the Auth class
    auth = Auth()
    # Ensure the user is logged out initially
    auth.logout()
    # Show the authentication menu
    auth_menu()
