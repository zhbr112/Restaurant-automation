import unittest
from src.settings import settings
from src.settings_maneger import settings_maneger


class test_settings(unittest.TestCase):
    
    def test_check_first_name(self):
        item = settings()
        
        item.name = "  Yaroslav  "
        
        assert item.name == "Yaroslav"

    def test_check_open_settings(self):
        maneger = settings_maneger()
        
        result=maneger.open("data/settings.json")

        assert result==True

    def test_check_open_settings2(self):
        maneger = settings_maneger()
        
        result=maneger.open("data/setingi.json")

        assert result==True

    def test_check_create_maneger(self):
        maneger1 = settings_maneger()
        maneger2 = settings_maneger()
        
        print(maneger1.unique_number)
        print(maneger2.unique_number)
        assert maneger1.unique_number==maneger2.unique_number

    def test_check_settings_data(self):
        maneger=settings_maneger()
        maneger.open("data/settings.json")

        params=maneger.data.keys()

        for param in params:
            assert getattr(maneger.settings,param)==maneger.data[param]
