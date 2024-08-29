from main_files.decorator.decorator_func import log_decorator


class Auth:
    @log_decorator
    def logout(self):
        pass

    @log_decorator
    def create_employee_table(self):
        pass
