import os
import json
import uuid
import pathlib
from src.settings import settings


class settings_maneger(object):
    # Имя файла настроек
    __file_name = ""
    # Уникальный номер
    __unique_number = None
    # Словарь с данными
    __data = {}
    
    # Настройки инстанс
    __settings = settings()

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(settings_maneger,cls).__new__(cls)
        return cls.instance     
        
    def __init__(self):
        self.__unique_number=uuid.uuid4()

    def __convert(self):
        if len(self.__data) == 0:
            raise Exception("Невозможно создать объект типа settings.py")
             
        params=self.data.keys()
        for param in params:
            setattr(self.settings,param,self.data[param])
            print(getattr(self.settings,param))

    @property
    def unique_number(self):
        return str(self.__unique_number.hex)
    
    @property
    def file_name(self):
        return self.__file_name
    
    @property
    def settings(self):
        return self.__settings
    
    @property
    def data(self):
        return self.__data

    def open(self,file_name:str):
        if not isinstance(file_name,str):
            raise Exception()
        
        if file_name=="":
            raise Exception()
        
        self.__file_name=file_name.strip()

        try:
            self.__open()
        except:
            raise Exception()
        self.__convert()       
        return True

    def __open(self):
        file_path=pathlib.Path.cwd()
        settings_file=f'{file_path}/{self.__file_name}'
        print(settings_file)

        if not os.path.exists(settings_file):
            raise Exception()
        
        with open(settings_file,"r") as read_file:
            self.__data=json.load(read_file)