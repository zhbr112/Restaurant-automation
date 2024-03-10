from src.Logics.report.report_abstract import report_abstract
from src.Logics.start_factory import start_factory
from src.argument_exception import arguent_exception
from src.Logics.report.convertor.convert_factory import convert_factory
import json


class report_json(report_abstract):

    def create(self, key: str):
        """
        Создание строки типа csv, с данными из storage
        """
        self.data = self.sdata.get(key)
        result=[]
        convert=convert_factory()
        for obj in self.data:
            result.append(convert.convert_obj(obj))

        rep_json=json.dumps(result,sort_keys = True, indent = 4)
        return(str(rep_json))