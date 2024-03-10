from src.Logics.report.report_csv import report_csv
from src.Logics.report.report_markdown import report_mardown
from src.Logics.report.report_json import report_json


class report_factory:
    __maps={}

    def __init__(self):
        self.__build_structure()

    def __build_structure(self):
        self.__maps['CSV']=report_csv
        self.__maps['markdown']=report_mardown 
        self.__maps['json']=report_json

    def create(self,settings, format, data):
        report_type =self.__maps[format]
        result=report_type(settings,data)
        return result