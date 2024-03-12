from src.models.unit_measurement_model import unit_measurement_model
from src.models.group_nomenclature_model import group_nomenclature_model
from src.models.storage_model import storage_model
from src.models.company_model import company_model
from src.models.nomenclature_model import nomenclature_model
from src.abstract_reference import abstract_reference
import datetime

class storage_tranzaction(abstract_reference):
    __storage:storage_model=None
    __nomenclature:nomenclature_model=None
    __count:int=0
    __unit_measurement:unit_measurement_model=None
    __period:datetime=None


    def __init__(self,storage,nomenclature,count,unit_measurement,period):
        self.__storage=storage
        self.__nomenclature=nomenclature
        self.__count=count
        self.__unit_measurement=unit_measurement
        self.__period=period


    @property
    def storage(self):
        return self.__storage

    @property
    def nomenclature(self):
        return self.__nomenclature

    @property
    def count(self):
        return self.__count

    @property
    def unit_measurement(self):
        return self.__unit_measurement

    @property
    def period(self):
        return self.__period