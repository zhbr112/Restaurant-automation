from src.models.unit_measurement_model import unit_measurement_model
from src.models.storage_model import storage_model
from src.models.nomenclature_model import nomenclature_model
from src.abstract_reference import abstract_reference
import datetime

class storage_tranzaction(abstract_reference):
    __storage:storage_model=None
    __nomenclature:nomenclature_model=None
    __count:int=0
    __unit_measurement:unit_measurement_model=None
    __period:datetime=None


    def __init__(self):
        super().__init__('storage_tranzaction')
        
    @staticmethod
    def create(storage,nomenclature,count,unit_measurement,period):
        obj=storage_tranzaction()
        obj.storage=storage
        obj.nomenclature=nomenclature
        obj.count=count
        obj.unit_measurement=unit_measurement
        obj.period=period
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
    def count(self):
        return self.__count
    
    @count.setter
    def count(self,value):
        self.__count=value

    @property
    def unit_measurement(self):
        return self.__unit_measurement
    
    @unit_measurement.setter
    def unit_measurement(self,value):
        self.__unit_measurement=value

    @property
    def period(self):
        return self.__period
    
    @period.setter
    def period(self,value):
        self.__period=value