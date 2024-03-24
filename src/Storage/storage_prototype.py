from src.argument_exception import arguent_exception
from datetime import datetime

class storage_prototype():
    __data = []

    def __init__(self, data: list) -> None:
        if len(data) <= 0:
            raise arguent_exception("Некорректно переданы параметры!")

        self.__data = data

    def filter(self, start_period: datetime, stop_period: datetime):
        if len(self.__data) <= 0:
            raise arguent_exception("Некорректно переданы параметры!")

        if start_period > stop_period:
            raise arguent_exception("Некорректный период!")

        result = []
        for item in self.__data:
            if item.period > start_period and item.period <= stop_period:
                result.append(item)

        return result

    def filter_nom(self, nomenclature):
        if len(self.__data) <= 0:
            raise arguent_exception("Некорректно переданы параметры!")

        result = []
        for item in self.__data:
            if item.nomenclature == nomenclature:
                result.append(item)

        return result