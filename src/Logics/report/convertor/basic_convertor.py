from src.Logics.report.convertor.convertor_abstrakt import convertor_abstrakt
from src.argument_exception import arguent_exception


class basic_convertor(convertor_abstrakt):
     
     def convert(self, obj):
        return str(obj)