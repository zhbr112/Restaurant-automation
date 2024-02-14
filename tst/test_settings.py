import unittest
from src.settings import settings
from src.settings_manager import settings_manager


class test_settings(unittest.TestCase):
    def test_check_name(self):
        item = settings()

        item.name = "  Yaroslav  "

        assert item.name == "Yaroslav"

    def test_check_type_ownership(self):
        item = settings()

        item.type_ownership = "   OOOOO   "

        assert item.type_ownership == "OOOOO"

    def test_check_create_maneger(self):
        manager1 = settings_manager()
        manager2 = settings_manager()

        assert manager1 is manager2

    def test_check_settings_data(self):
        manager = settings_manager()
        manager.open("config/settings.json")

        for key in manager.data.keys():
            if not hasattr(manager.settings, key):
                continue
            assert getattr(manager.settings, key) == manager.data[key]
