from src.Logics.report.convertor.convertor_abstrakt import convertor_abstrakt

class list_convertor(convertor_abstrakt):

    @classmethod
    def convert(cls, obj):
        from src.Logics.report.convertor.convert_factory import convert_factory
        return [convert_factory.convert_obj(unit_in_list) for unit_in_list in obj]