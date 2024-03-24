from src.Logics.report.convertor.convertor_abstrakt import convertor_abstrakt

class dict_convertor(convertor_abstrakt):

    @classmethod
    def convert(cls, obj):
        from src.Logics.report.convertor.convert_factory import convert_factory
        return {unit_in_list:convert_factory.convert_obj(obj[unit_in_list]) for unit_in_list in obj}