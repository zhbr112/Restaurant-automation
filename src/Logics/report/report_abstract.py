from src.Logics.start_factory import start_factory
from abc import ABC, abstractmethod

class report_abstract(ABC):
    __settings = None
    __sdata=None

    def __init__(self, settings, sdata):
        self.__settings=settings
        self.sdata=sdata

    @abstractmethod
    def create(self,key)->str:
        pass
        
    @property
    def settings(self):
        return self.__settings
    
    @property
    def sdata(self):
        return self.__sdata
    
    @sdata.setter
    def sdata(self, value):
        self.__sdata=value