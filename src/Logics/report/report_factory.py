from src.Logics.report.report_abstract import report_abstract
from src.Logics.report.report_csv import report_csv

class report_factory:
    __maps={}
    __data=None

    def __init__(self):
        self.__build_structure()

    def __build_structure(self):
        self.__maps['CSV']=report_csv
        self.__maps['markdown']=report_mardown 

    def create(self,settings, format, data):
        report_type =self.__maps[format]
        result=report_type(settings,data)
        return result