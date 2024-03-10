from src.Logics.report.convertor.convertor_abstrakt import convertor_abstrakt
from datetime import datetime


class datetime_convertor(convertor_abstrakt):

    @classmethod
    def convert(cls, obj: datetime):
        return {"Год":obj.year,
                "Месяц":obj.month,
                "День":obj.day,
                "Час":obj.hour,
                "Минуты":obj.minute,
                "Секунды":obj.second}