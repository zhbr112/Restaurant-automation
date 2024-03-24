from src.models.unit_measurement_model import unit_measurement_model
from src.models.storage_model import storage_model
from src.models.nomenclature_model import nomenclature_model
from src.abstract_reference import abstract_reference
import datetime

class storage_turn_model(abstract_reference):
    __storage:storage_model=None
    __nomenclature:nomenclature_model=None
    __turn:int=None
    __unit_measurement:unit_measurement_model=None

    def __init__(self):
        super().__init__('storage_turn_model')

    @staticmethod
    def create(storage,nomenclature,turn,unit_measurement):
        obj=storage_turn_model()
        obj.storage=storage
        obj.nomenclature=nomenclature
        obj.turn=turn
        obj.unit_measurement=unit_measurement
        return obj
    
    @property
    def storage(self):
        return self.__storage
    
    @storage.setter
    def storage(self,value):
        self.__storage=value

    @property
    def nomenclature(self):
        return self.__nomenclature
    
    @nomenclature.setter
    def nomenclature(self,value):
        self.__nomenclature=value

    @property
    def turn(self):
        return self.__turn
    
    @turn.setter
    def turn(self,value):
        self.__turn=value

    @property
    def unit_measurement(self):
        return self.__unit_measurement
    
    @unit_measurement.setter
    def unit_measurement(self,value):
        self.__unit_measurement=value