from src.error_proxy import error_proxy
from src.argument_exception import arguent_exception
from src.settings import settings
import unittest

# Действие


class test_error(unittest.TestCase):
    def test_check_set_error_text(self):
        # Подготовка
        error = error_proxy("Test", "Test")

        # Действие

        # Проверка
        assert error.is_error == True

    def test_check_set_error_zero(self):
        # Подготовка
        error = error_proxy()

        # Действие
        try:
            result = 1 / 0
        except Exception as ex:
            error.set_error(ex)

        # Проверка
        assert error.is_error == True

    def test_check_argument_exception(self):
        # Подготовка
        try:
            raise arguent_exception("Test")

        # Действие
        except arguent_exception as ex:
            print(ex.error.error_text)
            print(ex.error.error_source)

            # Проверка
            assert ex.error.is_error

    def test_check_settings(self):
        # Подготовка
        item = settings()

        # Действие
        try:
            item.INN = "112"
        except arguent_exception as ex:
            print(ex.error.error_text)
            print(ex.error.error_source)

            # Проверка
            assert ex.error.is_error