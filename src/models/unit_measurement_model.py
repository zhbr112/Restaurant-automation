from src.abstract_reference import abstract_reference
from src.argument_exception import arguent_exception
from src.error_proxy import error_proxy
from datetime import datetime
import random


# Единица измерения
class unit_measurement_model(abstract_reference):
    # Название единицы измерения
    __name_measurement = None
    # Коэффициент пересчета
    __conversion_factor: int = None
    # Базовая единица измерения
    __basic_unit_measurement = None
    
    __date_time=None
    # Инициализация объекта класса
    def __init__(
        self,
        name_measurement: str = None,
        conversion_factor: int = None,
        basic_unit_measurement=None
    ):
        super().__init__("unit_measurement_model")
        self.name_measurement = name_measurement
        self.conversion_factor = conversion_factor
        self.__basic_unit_measurement=basic_unit_measurement
        self.date_time=datetime.strptime(f'2024-{random.randint(1,12)}-{random.randint(1,28)} {random.randint(0,23)}:{random.randint(0,59)}:{random.randint(0,59)}.0', '%Y-%m-%d %H:%M:%S.%f')
        
        

    @property
    def name_measurement(self):
        return self.__name_measurement

    @name_measurement.setter
    def name_measurement(self, value: str):
        """
            Базовая единица измерения
        Args:
            value (str): Базовая единица измерения
        """

        self._validate(value, str)
        self.__name_measurement = value

    @property
    def date_time(self):
        return self.__date_time

    @date_time.setter
    def date_time(self, value: str):
        self.__date_time = value

    @property
    def conversion_factor(self):
        return self.__conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, value: int):
        """
            Коэффициент пересчета
        Args:
            value (str): Коэффициент пересчета
        """

        if value<=0:
            raise arguent_exception('Неверный коэфицент пересчета')
        self._validate(value, int)
        self.__conversion_factor = value

    @property
    def basic_unit_measurement(self):
        return self.__basic_unit_measurement
    
    @classmethod
    def create_gramm(cls):
        if not hasattr(cls, "gramm"):
            cls.gramm = unit_measurement_model('грамм', 1, None)
        return cls.gramm
    
    @classmethod
    def create_killogramm(cls):
        if not hasattr(cls, "killogramm"):
            base=unit_measurement_model.create_gramm()
            cls.killogramm=unit_measurement_model('киллограмм', 1000, base)
        return cls.killogramm

    
    @classmethod
    def create_thing(cls):
        if not hasattr(cls, "thing"):
            cls.thing=unit_measurement_model('шт', 1, None)
        return cls.thing

    
    @classmethod
    def create_mililitr(cls):
        if not hasattr(cls, "mililitr"):
            cls.mililitr=unit_measurement_model('мл', 1, None)
        return cls.mililitr
    
    @classmethod
    def create_litr(cls):
        if not hasattr(cls, "litr"):
            base=unit_measurement_model.create_mililitr()
            cls.litr=unit_measurement_model('литр', 1000, base)
        return cls.litr