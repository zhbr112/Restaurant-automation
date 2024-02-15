from src.abstract_reference import abstract_reference
from src.error_proxy import error_proxy
from src.models.unit_measurement_model import unit_measurement_model
from src.models.group_nomenclature_model import group_nomenclature_model


# Номенклатура
class nomenclature_model(abstract_reference):
    # Полное наименование
    __full_name = None

    # Инициализация объекта класса
    def __init__(self, full_name=None) -> None:
        super().__init__("nomenclature_model")
        self.full_name = full_name

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str = None):
        """
            Полное наименование
        Args:
            value (str): Полное наименование, не более 255 символов
        """
        self._validate(value, str, 255)
        self.__full_name = value