from src.Logics.report.convertor.convertor_abstrakt import convertor_abstrakt
from src.Logics.report.convertor.datetime_convertor import datetime_convertor
import uuid
from datetime import datetime
from src.abstract_reference import abstract_reference



class reference_convertor(convertor_abstrakt):

    @classmethod
    def convert(cls, obj):
        from src.Logics.report.convertor.convert_factory import convert_factory
        result = {}
        if isinstance(obj,(str,int,uuid.UUID)) or obj is None:
                    return obj
        
        for key in vars(obj):
            if len(key.split("__"))==1:
                continue
            
            key=key.split("__")[1]
            if hasattr(obj, key):
                unit=getattr(obj, key)
                result[key.capitalize().replace("_", " ")]=convert_factory.convert_obj(unit)
                
        return result