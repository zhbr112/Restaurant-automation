import os, json, pathlib, uuid
from src.settings import settings
from src.argument_exception import arguent_exception


class settings_manager:
    # Путь до файла настроек и имя самого файла
    __file_name = ""
    # Словарь с данными
    __data = {}
    # Объект настроект
    __settings = settings()
    # Уникальный номер
    __id: uuid.UUID

    # Если инстанс существует возращаем его, если нет то создаем. (singleton)
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    # Инициализация объекта класса
    def __init__(self):
        self.__id = uuid.uuid4()
        self.open("config/settings.json")

    def open(self, file_name: str):
        """
            Открытие файла с настройками
        Args:
            file_name (str): Путь до файла настроек и имя самого файла

        Raises:
            arguent_exception: Неверный тип аргумента
            arguent_exception: Неверная длина аргумента
        """

        # Проверяем, что бы путь был str
        if not isinstance(file_name, str):
            raise arguent_exception("Неверный тип аргумента")

        # Проверяем, что бы путь не был пуст
        if file_name == "":
            raise arguent_exception("Неверная длина аргумента")

        # Убираем лишние пробелы
        self.__file_name = file_name.strip()

        # Отлавливаем ошибки
        try:
            self.__open()
        except:
            raise arguent_exception("Неудалось открыть и считать файл")

        # Заполенние объекта настроек
        return True

    def __open(self):
        """
            Открытие файла настроек
        Raises:
            arguent_exception: Ошибка при открытии файла
        """

        # Получаем полный путь к файлу
        settings_file = f"{pathlib.Path.cwd()}/{self.__file_name}"

        # Проверяем существует ли файл по данному пути
        if not os.path.exists(settings_file):
            raise arguent_exception("Невозможно загрузить файл настроек")

        # Открываем файл и читаем json
        with open(settings_file, "r") as read_file:
            self.__data = json.load(read_file)
        self.__convert()

    def __convert(self):
        """
            Заполенние объекта настроек
        Raises:
            arguent_exception: Невозможно создать объект настроек
        """
        # Проверяем, что бы словарь не был пуст
        if len(self.__data) == 0:
            raise arguent_exception("Невозможно создать объект настроек")

        # Идем по всем ключам полученным из файла, и если у
        # объекта настроект есть это поле, заполняем его
        for key in self.data.keys():
            if not hasattr(self.settings, key):
                continue
            setattr(self.settings, key, self.data[key])

    @property
    def file_name(self):
        return self.__file_name

    @property
    def settings(self):
        return self.__settings

    @property
    def data(self):
        return self.__data