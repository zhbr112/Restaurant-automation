import unittest
from src.Logics.process_storage_turn import process_storage_turn
from src.Logics.start_factory import start_factory
from src.Logics.process_factory import process_factory
from src.Storage.storage import storage


class test_turn(unittest.TestCase):
    def test_turn(self):
        proces=process_factory().create(storage.process_turn_key(),start_factory().storage.data[storage.jornal_key()])
        assert proces != []