from src.argument_exception import arguent_exception
from datetime import datetime

class storage_prototype():
    __data = []

    def __init__(self, data: list) -> None:
        if len(data) <= 0:
            raise arguent_exception("Некорректно переданы параметры!")

        self.__data = data

    def filter_date(self, start_period: datetime, stop_period: datetime):
        if len(self.__data) <= 0:
            raise arguent_exception("Некорректно переданы параметры!")

        if start_period > stop_period:
            raise arguent_exception("Некорректный период!")

        result = []
        for item in self.__data:
            if item.period > start_period and item.period <= stop_period:
                result.append(item)

        self.__data=result
        return self.__data

    def filter_nom(self, nomenclature_name):
        if len(self.__data) <= 0:
            raise arguent_exception("Некорректно переданы параметры!")

        result = []
        print([i.nomenclature.id for i in self.data])
        for item in self.__data:
            if item.nomenclature.full_name == nomenclature_name:
                result.append(item)

        self.__data=result
        return self.__data
    
    def filter_storage(self, storage_name):

        result = []
        for item in self.__data:
            if item.storage.name == storage_name:
                result.append(item)

        self.__data=result
        return self.__data
    
    def filter_receipt(self, receipt):
        if len(self.__data) <= 0:
            raise arguent_exception("Некорректно переданы параметры!")

        result = []
        nomenclatures=[receipt.rows[nom].nomenclature.full_name for nom in receipt.rows]
        for item in self.__data:
            if item.nomenclature.full_name in nomenclatures:
                result.append(item)

        self.__data=result
        return self.__data
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data=value