from src.abstract_reference import abstract_reference
from src.argument_exception import arguent_exception
from src.error_proxy import error_proxy


# Единица измерения
class unit_measurement_model(abstract_reference):
    # Название единицы измерения
    __name_measurement = None
    # Коэффициент пересчета
    __conversion_factor: int = None
    # Базовая единица измерения
    __basic_unit_measurement = None

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
        self.__basic_unit_measurement=self
        
        if basic_unit_measurement is not None:
            self.__basic_unit_measurement=basic_unit_measurement

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