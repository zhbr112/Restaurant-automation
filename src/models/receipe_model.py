from src.abstract_reference import abstract_reference
from src.models.receipe_row_model import receipe_row_model



class receipe_model(abstract_reference):
    # Вес брутто
    _brutto: int = 0
    
    # Вес нетто
    _netto: int = 0

    # Состав рецепта
    _rows = {}
    
    # Инструкции
    _instructions = list()
    
    # Описание
    _comments: str = ""
    
    def __init__(self):
        super().__init__('receipe_model')

    def add(self, row: receipe_row_model):
        """
            Добавить состав блюда
        """
        self._rows[row.name_receipe] = row
        self.__calc_brutto()
        

    def __calc_brutto(self):
        """
            Перерасчет брутто
        """
        self._brutto = 0
        for position  in self._rows:
            self._brutto += self._rows[position].size 
            
    @property         
    def netto(self):
        return self._netto                        
        
    @netto.setter
    def netto(self, value: int):
        """
            Вес нетто
        """
        self._netto = value
        
    @property    
    def instructions(self):
        """
           Инструкция для приготовления
        """
        return self._instructions  
    
    @property
    def comments(self):
        return self._comments
    
    @comments.setter
    def comments(self, value: str):
        """
            Описание блюда
        """
        self._comments = value   
    
    
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
                    unit = i.unit_measurement.basic_unit_measurement   
            
            # Создаем запись в рецепте
            row = receipe_row_model(nomenclature, size, unit)
            receipt.add(row)
        
        return receipt