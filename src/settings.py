class settings:
    __first_name = ""
    __INN=None
    __BIK=None
    __score=None
    __cor_score=None
    __name=""
    __type_ownership=""

    @property
    def INN(self):
        return self.__INN
    
    @INN.setter
    def INN(self, value: int): 

        if not isinstance(value, int) or len(str(value))!=12:
            raise Exception("Некорректный аргумент!")
        
        self.__INN = value


    @property
    def BIK(self):
        return self.__BIK
    
    @BIK.setter
    def BIK(self, value: int):

        if not isinstance(value, int) or len(str(value))!=9:
            raise Exception("Некорректный аргумент!")
        
        self.__BIK = value


    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value: int):

        if not isinstance(value, int) or len(str(value))!=11:
            raise Exception("Некорректный аргумент!")
        
        self.__score = value


    @property
    def cor_score(self):
        return self.__cor_score
   
    @cor_score.setter
    def cor_score(self, value: int):

        if not isinstance(value, int) or len(str(value))!=11:
            raise Exception("Некорректный аргумент!")
        
        self.__cor_score = value


    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):

        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self.__name = value.strip()


    @property
    def type_ownership(self):
        return self.__type_ownership
    
    @type_ownership.setter
    def type_ownership(self, value: str):

        if not isinstance(value, str) or len(value.strip())>5:
            raise Exception("Некорректный аргумент!")
        
        self.__type_ownership = value.strip()