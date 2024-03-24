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

    def filter_nom(self, nomenclature_id):
        if len(self.__data) <= 0:
            raise arguent_exception("Некорректно переданы параметры!")

        result = []
        for item in self.__data:
            if item.nomenclature.id == nomenclature_id:
                result.append(item)

        self.__data=result
        return self.__data
    
    def filter_storage(self, storage_id):

        result = []
        for item in self.__data:
            if item.storage.id == storage_id:
                result.append(item)

        return result
    
    def filter_receipt(self, receipt):
        if len(self.__data) <= 0:
            raise arguent_exception("Некорректно переданы параметры!")

        result = []
        nomenclatures=(receipt.rows[nom].nomenclature.id for nom in receipt.rows)
        for nom in nomenclatures:
            prorotype=storage_prototype(self.__data)
            result+=prorotype.filter_nom(nom)

        self.__data=result
        return self.__data