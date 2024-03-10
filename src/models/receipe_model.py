from src.abstract_reference import abstract_reference
from src.models.receipe_row_model import receipe_row_model


class receipe_model(abstract_reference):
    # Вес брутто
    __brutto: int = 0
    
    # Вес нетто
    __netto: int = 0

    # Состав рецепта
    __rows = {}
    
    # Инструкции
    __instructions = list()
    
    # Описание
    __comments: str = ""
    
    def __init__(self):
        super().__init__('receipe_model')
        self.__brutto: int = 0
        self.__netto: int = 0
        self.__rows = {}
        self.__instructions = list()
        self.__comments: str = ""            
       
    @staticmethod
    def create_receipt(comments: str, items: list, data):
        """
            Фабричный метод. Сформировать рецепт
        Args:
            name (str): Наименование рецепта
            comments (str): Приготовление
            items (list): Состав рецепта
            data (list): Список номенклатуры
        """
        
        # Подготовим словарь со списком номенклатуры
        nomenclatures = data.list_positions
        receipt = receipe_model()
        for position in items:
            # Получаем список кортежей и берем первое значение
            _list =  list(position.items())        
            tuple = list(_list)[0]         
            nomenclature_name = tuple[0]
            size = tuple[1]
            for i in nomenclatures:
                if i.full_name==nomenclature_name:
                    nomenclature = i
                    if i.unit_measurement.basic_unit_measurement is not None:
                        unit = i.unit_measurement.basic_unit_measurement
                    else:
                        unit = i.unit_measurement
            
            # Создаем запись в рецепте
            row = receipe_row_model(nomenclature, size, unit)
            receipt.add(row)
        
        return receipt
    
    def add(self, row: receipe_row_model):
        """
            Добавить состав блюда
        """
        self.__rows[row.nomenclature.full_name] = row
        self.__calc__brutto()
        

    def __calc__brutto(self):
        """
            Перерасчет брутто
        """
        self.__brutto = 0
        for position  in self.__rows:
            self.__brutto += self.__rows[position].size   
    
    @property
    def rows(self):
        return self.__rows
    
    @property         
    def brutto(self):
        return self.__brutto
    
    @property         
    def netto(self):
        return self.__netto                        
        
    @netto.setter
    def netto(self, value: int):
        """
            Вес нетто
        """
        self.__netto = value
        
    @property    
    def instructions(self):
        """
           Инструкция для приготовления
        """
        return self.__instructions  
    
    @property
    def comments(self):
        return self.__comments
    
    @comments.setter
    def comments(self, value: str):
        """
            Описание блюда
        """
        self.__comments = value