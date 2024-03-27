from src.abstract_reference import abstract_reference
from src.error_proxy import error_proxy


# Склад
class storage_model(abstract_reference):
    __address=''
    __name=''

    # Инициализация объекта класса
    def __init__(self, name, address) -> None:
        super().__init__("storage_model")
        self.__address=address
        self.__name=name

    @property
    def address(self):
        return self.__address
    
    @property
    def name(self):
        return self.__name
    
    @staticmethod
    def strorage_irk():
        return storage_model('Главный', 'г. Иркутск, ул. Лермонтова, д. 126')
    
    @staticmethod
    def strorage_no_irk():
        return storage_model('Дополнительный', 'г. Ангарск, ул. Московская, д. 1')