from src.abstract_reference import abstract_reference
from src.error_proxy import error_proxy


class storage_model(abstract_reference):
    def __init__(self, full_name=None) -> None:
        super().__init__('storage_model')
