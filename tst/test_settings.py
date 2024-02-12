import unittest
from src.settings import settings
from src.settings_maneger import settings_maneger


class test_settings(unittest.TestCase):
    def test_check_name(self):
        item = settings()

        item.name = "  Yaroslav  "

        assert item.name == "Yaroslav"

    def test_check_type_ownership(self):
        item = settings()

        item.type_ownership = "    OOOOO    "

        assert item.type_ownership == "OOOOO"

    def test_check_create_maneger(self):
        maneger1 = settings_maneger()
        maneger2 = settings_maneger()

        assert maneger1 is maneger2

    def test_check_settings_data(self):
        maneger = settings_maneger()
        maneger.open("config/settings.json")

        for key in maneger.data.keys():
            if not hasattr(maneger.settings, key):
                continue
            assert getattr(maneger.settings, key) == maneger.data[key]
