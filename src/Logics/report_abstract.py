from src.Logics.start_factory import start_factory


class report_abstract:
    __settings = None
    __sdata=None

    def __init__(self, settings, sdata):
        self.__settings=settings
        self.sdata=sdata

    def create(self,key)->str:
        pass

    def create_str(self,key)->str:
        str_=''
        str_+=(
            ";".join(
                [
                    unit.split("__")[1].capitalize().replace("_", " ")
                    for unit in vars(self.data[0])
                ]
            )
            + "|"
        )
        
    @property
    def settings(self):
        return self.__settings
    
    @property
    def sdata(self):
        return self.__sdata
    
    @sdata.setter
    def sdata(self, value):
        self.__sdata=value