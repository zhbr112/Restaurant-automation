from src.abstract_reference import abstract_reference
from src.argument_exception import arguent_exception
from src.error_proxy import error_proxy


# Единица измерения
class unit_measurement_model(abstract_reference):
    # Базовая единица измерения
    __basic_unit_measurement: str = None
    # Коэффициент пересчета
    __conversion_factor: int = None
    # Родитель
    __parent = None

    # Инициализация объекта класса
    def __init__(
        self,
        basic_unit_measurement: str = None,
        conversion_factor: int = None,
        parent=None,
    ):
        super().__init__("unit_measurement_model")
        self.basic_unit_measurement = basic_unit_measurement
        self.conversion_factor = conversion_factor
        self.__parent = parent

    @property
    def basic_unit_measurement(self):
        return self.__basic_unit_measurement

    @basic_unit_measurement.setter
    def basic_unit_measurement(self, value: str):
        """
            Базовая единица измерения
        Args:
            value (str): Базовая единица измерения
        """

        self._validate(value, str)
        self.__basic_unit_measurement = value

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

        self._validate(value, int)
        self.__conversion_factor = value

    @property
    def parent(self):
        return self.__parent