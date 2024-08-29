from main_files.decorator.decorator_func import log_decorator


class EmployeeForCompany:
    @log_decorator
    def create_employee(self):
        pass
