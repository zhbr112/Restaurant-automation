from src.abstract_reference import abstract_reference
from src.models.receipe_row_model import receipe_row_model



class receipe_model(abstract_reference):
    # Вес брутто
    _brutto: int = 0
    
    # Вес нетто
    _netto: int = 0

    # Состав рецепта
    _rows = list()
    
    # Инструкции
    _instructions = list()
    
    # Описание
    _comments: str = ""
    
    def add(self, row: receipe_row_model):
        """
            Добавить состав блюда
        """
        self._rows[row.name] = row
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
    def create_receipt(comments: str, items: list, data: list):
        """
            Фабричный метод. Сформировать рецепт
        Args:
            name (str): Наименование рецепта
            comments (str): Приготовление
            items (list): Состав рецепта
            data (list): Список номенклатуры
        """
        
        
        # Подготовим словарь со списком номенклатуры
        nomenclatures = data  
        receipt = receipe_model()
        
        for position in items:
            # Получаем список кортежей и берем первое значение
            _list =  list(position.items())        
            tuple = list(_list)[0]         
            nomenclature_name = tuple[0]
            size = tuple[1]          
            nomenclature = nomenclatures[nomenclature_name]
            
            # Определяем единицу измерения
            if nomenclature.unit.base_unit is None:
                unit = nomenclature.unit
            else:
                unit = nomenclature.unit.base_unit    
            
            # Создаем запись в рецепте
            row = receipe_row_model(nomenclature, size, unit)
            receipt.add(row)
        
        return receipt