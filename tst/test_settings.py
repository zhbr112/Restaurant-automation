import unittest
from src.settings import settings
from src.settings_manager import settings_manager


class test_settings(unittest.TestCase):
    def test_check_name(self):
        # Подготовка
        item = settings()

        # Действие
        item.name = "  Yaroslav  "

        # Проверка
        assert item.name == "Yaroslav"

    def test_check_type_ownership(self):
        # Подготовка
        item = settings()

        # Действие
        item.type_ownership = "   OOOOO   "

        # Проверка
        assert item.type_ownership == "OOOOO"

    def test_check_create_maneger(self):
        # Подготовка
        manager1 = settings_manager()
        manager2 = settings_manager()

        # Действие

        # Проверка
        assert manager1 is manager2

    def test_check_settings_data(self):
        # Подготовка
        manager = settings_manager()

        # Действие
        for key in manager.data.keys():
            if not hasattr(manager.settings, key):
                continue

            # Проверка
            assert getattr(manager.settings, key) == manager.data[key]
            print(getattr(manager.settings, key))