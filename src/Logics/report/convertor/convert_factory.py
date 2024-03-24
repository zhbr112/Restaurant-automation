from src.Logics.report.convertor.datetime_convertor import datetime_convertor
from src.Logics.report.convertor.basic_convertor import basic_convertor
from src.Logics.report.convertor.reference_convertor import reference_convertor
from src.Logics.report.convertor.list_convector import list_convertor
from src.Logics.report.convertor.dict_convector import dict_convertor
from datetime import datetime
import uuid
from src.abstract_reference import abstract_reference


class convert_factory:
    __maps={}
    __maps[int] = basic_convertor
    __maps[uuid.UUID] = basic_convertor
    __maps[str] = basic_convertor
    __maps[type(None)] = basic_convertor
    __maps[list] = list_convertor
    __maps[dict] = dict_convertor
    __maps[datetime] = datetime_convertor
    for classes in abstract_reference.__subclasses__():
        __maps[classes] = reference_convertor

    @classmethod
    def convert_obj(self, obj):
        converter = self.__maps[type(obj)]()
        return converter.convert(obj)     