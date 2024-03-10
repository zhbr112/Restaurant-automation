class storage:
    __data={}

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance
    
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
    def group_key():
        return "group"
    
    @staticmethod
    def receipt_key():
        return "receipts"