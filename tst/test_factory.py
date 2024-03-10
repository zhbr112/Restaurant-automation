from src.models.unit_measurement_model import unit_measurement_model
from src.Logics.start_factory import start_factory
from src.settings_manager import settings_manager
from src.Logics.report.report_csv import report_csv
from src.Logics.report.report_factory import report_factory
from src.Logics.report.report_json import report_json
from src.Logics.report.report_markdown import report_mardown
from src.Storage.storage import storage
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

    def test_check__factory_create_receipe(self):
        assert start_factory.create_receipts()[0]._rows['Мука пшеничная'].size == 100

    def test_check__factory_create_receipe_all(self):
        items = [
            {"Мука пшеничная": 100},
            {"Сахар": 80},
            {"Сливочное масло": 70},
            {"Яйца": 1},
            {"Ванилин": 5},
        ]
        for i in items:
            assert start_factory.create_receipts()[0]._rows[list(i.items())[0][0]].nomenclature.full_name == list(i.items())[0][0]
            assert start_factory.create_receipts()[0]._rows[list(i.items())[0][0]].size == list(i.items())[0][1]


        items = [
            {"Куриное филе": 200},
            {"Салат Романо": 50},
            {"Сыр Пармезан": 50},
            {"Чеснок": 10},
            {"Белый хлеб": 30},
            {"Соль": 5},
            {"Черный перец": 2},
            {"Оливковое масло": 10},
            {"Лимонный сок": 5},
            {"Горчица дижонская": 5},
            {"Яйца": 2},
        ]
        for i in items:
            assert start_factory.create_receipts()[1]._rows[list(i.items())[0][0]].nomenclature.full_name == list(i.items())[0][0]
            assert start_factory.create_receipts()[1]._rows[list(i.items())[0][0]].size == list(i.items())[0][1]


        items = [
            {"Яйца": 3},
            {"Сахарная пудра": 180},
            {"Ванилин": 5},
            {"Корица": 5},
            {"Какао": 20},
        ]

        for i in items:
            assert start_factory.create_receipts()[2]._rows[list(i.items())[0][0]].nomenclature.full_name == list(i.items())[0][0]
            assert start_factory.create_receipts()[2]._rows[list(i.items())[0][0]].size == list(i.items())[0][1]

    def test_check_report_csv(self):
        data = start_factory().storage.data
        settings=settings_manager().settings
        report_csv_=report_mardown(settings,data)
        print(report_csv_.create(storage.measurement_key()))
        print(report_csv_.create(storage.group_key()))
        print(report_csv_.create(storage.nomenculature_key()))
        assert report_csv_.create(storage.group_key())!=''
        assert report_csv_.create(storage.measurement_key())!=''
        assert report_csv_.create(storage.nomenculature_key())!=''

    def test_check_report_factory_csv(self):
        settings=settings_manager().settings
        data = start_factory().storage.data
        report=report_factory()
        format="CSV"
        print(report.create(settings,format,data).create(storage.measurement_key()))


