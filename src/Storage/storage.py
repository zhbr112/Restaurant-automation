class storage:
    __data={}

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        self.data[storage.measurement_key()]=[]
        self.data[storage.nomenculature_key()]=[]
        self.data[storage.group_key()]=[]
        self.data[storage.receipt_key()]=[]
        self.data[storage.storage_key()]=[]
    
    @property
    def data(self)->dict:
        return self.__data
    
    @staticmethod
    def nomenculature_key():
        return 'nomeculature'
    
    @staticmethod
    def measurement_key():
        return "measurement"
    
    @staticmethod
    def storage_key():
        return "storage"
    
    @staticmethod
    def group_key():
        return "group"
    
    @staticmethod
    def receipt_key():
        return "receipts"
    
    @staticmethod
    def jornal_key():
        return "jornal"
    
    @staticmethod
    def  process_turn_key():
        return "process_storage_turn"