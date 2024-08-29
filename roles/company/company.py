from main_files.decorator.decorator_func import log_decorator
from roles.company.department import Department


class Company:
    def __init__(self):
        self.__department = Department()

    @log_decorator
    def create_department(self):
        self.__department.create_department()
        return True
