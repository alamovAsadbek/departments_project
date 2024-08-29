from main_files.decorator.decorator_func import log_decorator
from roles.company.department import Department
from roles.company.employee import EmployeeForCompany


class Company:
    def __init__(self):
        self.__department = Department()
        self.__employee = EmployeeForCompany()

    @log_decorator
    def create_department(self):
        self.__department.create_department()
        return True

    @log_decorator
    def show_department(self):
        self.__department.show_department()
        return True

    @log_decorator
    def update_department(self):
        self.__department.update_department()
        return True

    @log_decorator
    def delete_department(self):
        self.__department.delete_department()
        return True

    @log_decorator
    def create_employee(self):
        self.__employee.create_employee()
        return True
