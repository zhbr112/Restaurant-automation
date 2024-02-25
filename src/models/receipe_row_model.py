from src.abstract_reference import abstract_reference
from src.models.unit_measurement_model import unit_measurement_model
from src.models.nomenclature_model import nomenclature_model
from src.argument_exception import arguent_exception


# Номенклатура
class receipe_row_model(abstract_reference):
    __nomenclature:nomenclature_model=None
    __size:int=0
    __unit:unit_measurement_model=None
    __name_receipe=''

    def __init__(self,nomenclature:nomenclature_model=None, size:int=0, unit:unit_measurement_model=None):
        super().__init__('receipe_row_model')
        self.nomenclature=nomenclature
        self.size=size
        self.unit=unit
        self.name_receipe=f'{self.__nomenclature.full_name}, {self.__nomenclature.unit_measurement.name_measurement}'
                                                             
    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self,value):
        self.__nomenclature=value
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,value):
        self.__size=value
    
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self,value):
        self.__unit=value
    
    @property
    def name_receipe(self):
        return self.__name_receipe

    @name_receipe.setter
    def name_receipe(self,value):
        self.__name_receipe=value