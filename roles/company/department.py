from main_files.decorator.decorator_func import log_decorator


class Department:
    @log_decorator
    def create_department(self):
        pass
