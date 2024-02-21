from src.models.unit_measurement_model import unit_measurement_model
from src.Logics.start_factory import start_factory
from src.settings import settings
from src.settings_manager import settings_manager
import unittest


class test_factory(unittest.TestCase):
    def test_check_factory(self):
        unit=unit_measurement_model.create_killogramm()

        assert unit is not None

    def test_check_group_nomenclature(self):
        group=start_factory.create_nomenclature()
        for item in group.list_positions:
            print(item.full_name,item.unit_measurement.name_measurement)

        assert len(group.list_positions)>0

    def test_check_factory_create_method(self):
        manager = settings_manager()
        manager.open("config/settings.json")
        factory=start_factory(manager.settings)

        assert len(factory.create_nomenclature().list_positions)>0
        assert factory.storage is not None
        assert factory.storage.data is not None
        print(factory.storage.data)
