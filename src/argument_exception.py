from src.error_proxy import error_proxy


class arguent_exception(Exception):
    # Объект класса внутренних ошибок
    __inner_error: error_proxy = error_proxy()

    # Инициализация объекта класса
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        # устанвливаем ошибку
        self.__inner_error.set_error(self)

    # Обращение к объекту класса внутренних ошибок
    @property
    def error(self):
        return self.__inner_error