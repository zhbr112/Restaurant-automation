class error_proxy:
    __error_text = ""
    __error_source = ""
    __is_error = False

    def __init__(self, error_text: str = "", error_source: str = ""):
        self.error_text = error_text
        self.error_source = error_source

    def __validate(self, value, type_, source) -> bool:

        # Проверка типа
        if not isinstance(value, type_):
            self.error_source = source

        # Проверка аргумента
        if len(str(value).strip()) == 0:
            return self.is_error

        return True

    @property
    def error_text(self):
        return self.__error_text

    @error_text.setter
    def error_text(self, value: str):
        if self.__validate(value, str, "error_text"):
            self.__error_text = value
            self.__is_error = True

    @property
    def error_source(self):
        return self.__error_source

    @error_source.setter
    def error_source(self, value: str):
        if self.__validate(value, str, "error_text"):
            self.__error_source = value
            self.__is_error = True

    @property
    def is_error(self):
        return self.__is_error

    def set_error(self, exception: Exception):
        self.__validate(exception, Exception, "set_error")

        if exception is not None:
            self.error_text = f"Ошибка: {str(exception)}"
            self.error_source = f"Исключение: {type(exception)}"
