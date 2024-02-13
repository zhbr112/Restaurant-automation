import uuid
from src.argument_exception import arguent_exception


class abstract_reference:
    __id: uuid.UUID
    __name: str = ""

    def __init__(self, name: str = None) -> None:
        self.name = name
        self.__id = uuid.uuid4

    def __validate(self, value, type_, source) -> bool:

        # Проверка типа
        if not isinstance(value, type_):
            raise arguent_exception("Некорректный тип")

        # Проверка аргумента
        if len(str(value).strip()) == 0:
            raise arguent_exception("Пустой аргумент")

        return True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__validate(value, str)
        self.__name = value.strip()
