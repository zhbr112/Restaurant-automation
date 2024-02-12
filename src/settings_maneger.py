import os, json, pathlib
from src.settings import settings


class settings_maneger(object):
    # Путь до файла настроек и имя самого файла
    __file_name = ""

    # Словарь с данными
    __data = {}

    # Объект настроект
    __settings = settings()

    # Если инстанс существует возращаем его, если нет то создаем. (singleton)
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(settings_maneger, cls).__new__(cls)
        return cls.instance

    def __convert(self):
        """
            Заполенние объекта настроек
        Raises:
            Exception: Невозможно создать объект настроек
        """
        # Проверяем, что бы словарь не был пуст
        if len(self.__data) == 0:
            raise Exception("Невозможно создать объект настроек")
        
        # Идем по всем ключам полученным из файла, и если у
        # объекта настроект есть это поле, заполняем его
        for key in self.data.keys():
            if not hasattr(self.settings, key):
                continue
            setattr(self.settings, key, self.data[key])

    def open(self, file_name: str):
        """
            Открытие файла с настройками
        Args:
            file_name (str): Путь до файла настроек и имя самого файла

        Raises:
            TypeError: Неверный тип аргумента
            ValueError: Неверная длина аргумента
        """

        # Проверяем, что бы путь был str
        if not isinstance(file_name, str):
            raise TypeError("Неверный тип аргумента")
        
        # Проверяем, что бы путь не был пуст
        if file_name == "":
            raise ValueError("Неверная длина аргумента")
        
        # Убираем лишние пробелы
        self.__file_name = file_name.strip()

        # Отлавливаем ошибки
        try:
            self.__open()
        except:
            raise Exception()
        
        # Заполенние объекта настроек
        self.__convert()
        return True

    def __open(self):
        """
            Открытие файла настроек
        Raises:
            FileNotFoundError: Ошибка при открытии файла
        """

        # Получаем полный путь к файлу
        settings_file = f"{pathlib.Path.cwd()}/{self.__file_name}"

        # Проверяем существует ли файл по данному пути
        if not os.path.exists(settings_file):
            raise FileNotFoundError("Невозможно загрузить файл настроек")
        
        # Открываем файл и читаем json
        with open(settings_file, "r") as read_file:
            self.__data = json.load(read_file)


    @property
    def file_name(self):
        return self.__file_name

    @property
    def settings(self):
        return self.__settings

    @property
    def data(self):
        return self.__data
