from src.abstract_reference import abstract_reference
from src.error_proxy import error_proxy


# Склад
class storage_model(abstract_reference):
    __address=''

    # Инициализация объекта класса
    def __init__(self, address) -> None:
        super().__init__("storage_model")
        self.__address=address

    @property
    def address(self):
        return self.__address
    
    @staticmethod
    def strorage_irk():
        return storage_model('г. Иркутск, ул. Лермонтова, д. 126')
    
    @staticmethod
    def strorage_no_irk():
        return storage_model('НЕ г. Иркутск, ул. Лермонтова, д. 126')