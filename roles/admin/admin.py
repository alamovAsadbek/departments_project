from main_files.decorator.decorator_func import log_decorator


class Admin:
    @log_decorator
    def create_new_company(self):
        pass
