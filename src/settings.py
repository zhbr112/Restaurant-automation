from src.argument_exception import arguent_exception

# Класс содержащий общие настройки приложения
class settings:
    # ИНН
    __INN = None
    # БИК
    __BIK = None
    # Счет
    __score = None
    # Корреспондентский счет
    __cor_score = None
    # Наименование
    __name = ""
    # Вид собственности
    __type_ownership = ""

    def __validate(self, value, type_=None, len_: int = None) -> bool:
        """
            Валидация аргумента по типу и дате
        Args:
            value (any): Аргумент
            type_ (any): Ожидаемый тип
            len_ (int): Ожидаемая длина

        Raises:
            arguent_exception: Некорректный тип
            arguent_exception: Некорректная длина

        Returns:
            True или Exception
        """

        # Проверка типа
        if type_ is not None and not isinstance(value, type_):
            raise arguent_exception("Некорректный тип")

        # Проверка аргумента
        if len_ is not None and len(str(value).strip()) != len_:
            raise arguent_exception("Некорректная длина")

        return True

    @property
    def INN(self):
        return self.__INN

    @INN.setter
    def INN(self, value: int):
        """
            ИНН
        Args:
            value (int): Значение ИНН, 12 символов

        Raises:
            arguent_exception: Некорректный тип аргумента
            arguent_exception: Некорректная длина аргумента
        """

        self.__validate(value, int, 12)
        self.__INN = value

    @property
    def BIK(self):
        return self.__BIK

    @BIK.setter
    def BIK(self, value: int):
        """
            БИК
        Args:
            value (int): Значение БИК, 9 символов

        Raises:
            arguent_exception: Некорректный тип аргумента
            arguent_exception: Некорректная длина аргумента
        """

        self.__validate(value, int, 9)
        self.__BIK = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value: int):
        """
            Счет
        Args:
            value (int): Номер счета, 11 символов

        Raises:
            arguent_exception: Некорректный тип аргумента
            arguent_exception: Некорректная длина аргумента
        """

        self.__validate(value, int, 11)
        self.__score = value

    @property
    def cor_score(self):
        return self.__cor_score

    @cor_score.setter
    def cor_score(self, value: int):
        """
            Корреспондентский счет
        Args:
            value (int): Номер Корреспондентского счета, 11 символов

        Raises:
            arguent_exception: Некорректный тип аргумента
            arguent_exception: Некорректная длина аргумента
        """

        self.__validate(value, int, 11)
        self.__cor_score = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        """
            Наименование
        Args:
            value (str): Наименование

        Raises:
            arguent_exception: Некорректный тип аргумента
        """

        self.__validate(value, str)
        self.__name = value.strip()

    @property
    def type_ownership(self):
        return self.__type_ownership

    @type_ownership.setter
    def type_ownership(self, value: str):
        """
            Вид собственности
        Args:
            value (str): Вид собственности, 5 символов

        Raises:
            arguent_exception: Некорректный тип аргумента
            arguent_exception: Некорректная длина аргумента
        """

        self.__validate(value, str, 5)
        self.__type_ownership = value.strip()
