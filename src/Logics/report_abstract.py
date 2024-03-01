from src.Logics.start_factory import start_factory


class report_abstract:
    __settings = None
    __data=None

    def __init__(self, settings):
        self.__settings=settings

    def create(self,data)->str:
        pass

    @property
    def settings(self):
        return self.__settings
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data=value