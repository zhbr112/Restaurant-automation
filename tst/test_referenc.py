from src.models.unit_measurement_model import unit_measurement_model
from src.Logics.start_factory import start_factory
from src.settings_manager import settings_manager
from src.Logics.report.report_csv import report_csv
from src.Logics.report.report_factory import report_factory
from src.Logics.report.report_json import report_json
from src.Logics.report.report_markdown import report_mardown
from src.Logics.report.convertor.reference_convertor import reference_convertor
from src.Storage.storage import storage
from src.Logics.report.convertor.convert_factory import convert_factory
import unittest

class test_referenc(unittest.TestCase):
    def test_check_referenc(self):
        q=reference_convertor()
        data=start_factory().storage.data
        w=convert_factory()
        print(w.convert_obj(data[storage.nomenculature_key()][0]))