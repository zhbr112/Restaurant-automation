from src.Logics.report.convertor.convertor_abstrakt import convertor_abstrakt
from datetime import datetime


class datetime_convertor(convertor_abstrakt):

    @classmethod
    def convert(cls, obj: datetime):
        return {"Year": obj.year,
                "Month": obj.month,
                "Day": obj.day,
                "Hour": obj.hour,
                "Minute": obj.minute,
                "Second": obj.second,
                }