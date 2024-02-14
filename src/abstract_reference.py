import uuid
from src.argument_exception import arguent_exception


class abstract_reference:
    __id: uuid.UUID
    __name_model: str = ""

    def __init__(self, name: str = None) -> None:
        self.name_model = name
        self.__id = uuid.uuid4()

    def _validate(self, value, type_, len_=None) -> bool:

        #Проверка типа
        if not isinstance(value, type_):
            raise arguent_exception("Некорректный тип")

        # Проверка аргумента
        if len(str(value).strip()) == 0:
            raise arguent_exception("Пустой аргумент")
        
        if len_ is not None and len(str(value).strip()) >=len_:
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
        self._validate(value, str, 50)
        self.__name_model = value
