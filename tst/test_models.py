from src.models.unit_measurement_model import unit_measurement_model
from src.models.group_nomenclature_model import group_nomenclature_model
from src.models.storage_model import storage_model
from src.models.company_model import company_model
from src.models.nomenclature_model import nomenclature_model
from src.settings_manager import settings_manager
import unittest


class test_models(unittest.TestCase):
    def test_check_set_settings_company(self):
        manager = settings_manager()
        manager.open("config/settings.json")
        company = company_model(manager.settings)
        for key in manager.data.keys():
            if not hasattr(company, key):
                continue
            print(key, getattr(company, key), manager.data[key])
            assert getattr(company, key) == manager.data[key]

    def test_check_unit_measurement_model(self):
        base_measurement = unit_measurement_model("грамм", 1)
        new_measurement = unit_measurement_model("кг", 1000, base_measurement)
        print(
            new_measurement.parent.basic_unit_measurement,
            base_measurement.basic_unit_measurement,
        )
        print(new_measurement.basic_unit_measurement)
        assert (
            new_measurement.parent.basic_unit_measurement
            == base_measurement.basic_unit_measurement
        )

    def test_check_models(self):
        try:
            unit_measurement1 = unit_measurement_model("грамм", 1)
            unit_measurement2 = unit_measurement_model("кг", 1000, unit_measurement1)
            group_nomenclature = group_nomenclature_model()
            storage = storage_model()
            nomenclature1 = nomenclature_model("1dsf")
            nomenclature2 = nomenclature_model("1dsfddfdsdsssssssssssssssssssf")

            assert True
            
        except:
            assert False
