from src.Logics.report.convertor.datetime_convertor import datetime_convertor
from src.Logics.report.convertor.basic_convertor import basic_convertor
from src.Logics.report.convertor.reference_convertor import reference_convertor
from datetime import datetime
from src.abstract_reference import abstract_reference


class convert_factory:
    __maps={}

    def __init__(self):
        self.__maps[datetime] = datetime_convertor()
        self.__maps[int] = basic_convertor()
        self.__maps[str] = basic_convertor()
        for classes in abstract_reference.__subclasses__():
            self.__maps[classes] = reference_convertor()

    def convert_obj(self, obj):
        converter = self.__maps[type(obj)]
        return converter.convert(obj)     