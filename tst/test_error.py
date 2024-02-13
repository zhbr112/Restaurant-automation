from src.error_proxy import error_proxy
from src.argument_exception import arguent_exception
from src.settings import settings
import unittest


class test_error(unittest.TestCase):
    def test_check_set_error_text(self):
        error = error_proxy("Test", "Test")

        assert error.is_error == True

    def test_check_set_error_zero(self):
        error = error_proxy()

        try:
            result = 1 / 0
        except Exception as ex:
            error.set_error(ex)

        assert error.is_error == True

    def test_check_argument_exception(self):
        try:
            raise arguent_exception("Test")
        except arguent_exception as ex:
            print(ex.error.error_text)
            print(ex.error.error_source)
            assert ex.error.is_error

    def test_check_settings(self):
        item = settings()
        try:
            item.INN = "112"
        except arguent_exception as ex:
            print(ex.error.error_text)
            print(ex.error.error_source)
            assert ex.error.is_error
