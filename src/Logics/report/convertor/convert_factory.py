
from src.Logics.report.convertor.datetime_convertor import datetime_convertor
from src.Logics.report.convertor.basic_convertor import basic_convertor
from src.Logics.report.convertor.reference_convertor import reference_convertor
import uuid
from datetime import datetime

from src.abstract_reference import abstract_reference

class convert_factory:
    converts = {}

    def __init__(self):
        self.converters = {
            int: basic_convertor(),
            str: basic_convertor(),
            datetime: datetime_convertor(),
        }

    def convert_obj(self, obj):
        obj_type = type(obj)
        if obj_type in self.converters:
            converter = self.converters[obj_type]
            return converter.convert(obj)
        else:
            converter = reference_convertor()
            return converter.convert(obj)
       