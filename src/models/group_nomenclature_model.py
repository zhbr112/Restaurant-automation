from src.abstract_reference import abstract_reference
from src.error_proxy import error_proxy


# Группа номенклатура
class group_nomenclature_model(abstract_reference):
    __list_positions=[]
    __name=[]

    # Инициализация объекта класса
    def __init__(self, name=None, list_positions=[]) -> None:
        super().__init__("group_nomenclature_model")
        self.list_positions=list_positions
        self.name=name

    @staticmethod
    def create_group():
        item=group_nomenclature_model("Ингредиенты")
        return item
    
    def append(self, unit):
        self.list_positions.append(unit)


    @property
    def list_positions(self):
        return self.__list_positions

    @list_positions.setter
    def list_positions(self, value=None):
        #self._validate(value, str, 255)
        self.__list_positions = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value=None):
        #self._validate(value, str, 255)
        self.__name = value