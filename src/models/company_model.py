from src.abstract_reference import abstract_reference
from src.argument_exception import arguent_exception
from src.error_proxy import error_proxy


# Компания
class company_model(abstract_reference):
    # ИНН
    __INN = None
    # БИК
    __BIK = None
    # Счет
    __score = None
    # Вид собственности
    __type_ownership = ""

    # Инициализация объекта класса
    def __init__(self, settings) -> None:
        super().__init__("organization_model")
        keys=[i for i in dir(self) if i[0]!='_']
        for key in keys:
            if hasattr(settings, key):
                setattr(self, f'_company_model__{key}', getattr(settings,key))

    @property
    def INN(self):
        return self.__INN

    @property
    def BIK(self):
        return self.__BIK

    @property
    def score(self):
        return self.__score

    @property
    def type_ownership(self):
        return self.__type_ownership