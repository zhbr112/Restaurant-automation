from src.Storage.storage import storage
from src.Logics.process_storage_turn import process_storage_turn


class process_factory:
    __maps={}

    def __init__(self):
        self.__build_structure()

    def __build_structure(self):
        self.__maps[storage.process_turn_key()]=process_storage_turn         

    def create(self, format, list_storage_tranzaction):
        return self.__maps[format].create((list_storage_tranzaction))