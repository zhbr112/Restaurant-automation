from abc import ABC, abstractmethod


class convertor_abstrakt(ABC):
    
    @abstractmethod
    def convert(self, obj):
        pass