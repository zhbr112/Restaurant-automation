from src.Logics.report.convertor.convertor_abstrakt import convertor_abstrakt
from src.Logics.report.convertor.datetime_convertor import datetime_convertor
import uuid
from datetime import datetime

class reference_convertor(convertor_abstrakt):

    @classmethod
    def convert(cls, obj):
        result = {}
        for key in vars(obj):
            key=key.split("__")[1]
            if hasattr(obj, key):
                unit=getattr(obj, key)
                if isinstance(unit,datetime):
                    result[key.capitalize().replace("_", " ")]=datetime_convertor.convert(unit)
                elif isinstance(unit,(str,int,uuid.UUID)) or unit is None:
                    result[key.capitalize().replace("_", " ")]=str(unit)
                elif isinstance(unit,list):
                    result[key.capitalize().replace("_", " ")]=[cls.convert(unit_in_list) for unit_in_list in unit]
                else:
                    result[key.capitalize().replace("_", " ")]=cls.convert(unit)

        return result