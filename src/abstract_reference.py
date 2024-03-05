import uuid
from src.argument_exception import arguent_exception


class abstract_reference:
    # Уникальный номер
    __id: uuid.UUID=None
    # Имя модели
    __name_model: str = ""

    # Инициализация объекта класса
    def __init__(self, name: str = None) -> None:
        name_model = name
        if self.id is None:
            self.__id=uuid.uuid4()

    def _validate(self, value, type_, len_=None):
        """
            Валидация аргумента по типу и длине
        Args:
            value (any): Аргумент
            type_ (object): Ожидаемый тип
            len_ (int): Максимальная длина
        """

        # Проверка типа
        if not isinstance(value, type_):
            raise arguent_exception("Некорректный тип")

        # Проверка аргумента
        if len(str(value).strip()) == 0:
            raise arguent_exception("Пустой аргумент")

        if len_ is not None and len(str(value).strip()) >= len_:
            raise arguent_exception("Некорректная длина аргумента")

        return True

    @property
    def id(self):
        return self.__id

    @property
    def name_model(self):
        return self.__name_model

    @name_model.setter
    def name_model(self, value: str):
        """
            Имя модели
        Args:
            value (str): Имя модели, не более 50 символов
        """
        self._validate(value, str, 50)
        self.__name_model = value

    