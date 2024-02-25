from src.models.unit_measurement_model import unit_measurement_model
from src.models.group_nomenclature_model import group_nomenclature_model
from src.models.storage_model import storage_model
from src.models.company_model import company_model
from src.models.nomenclature_model import nomenclature_model
from src.settings_manager import settings_manager
from src.settings import settings
from src.Storage.storage import storage
from src.models.receipe_model import receipe_model

class start_factory:
    __settings:settings=None
    __storage:storage=None
    def __init__(self,settings:settings=None,storage:storage=None):
        self.__settings=settings
        self.__storage=storage
        self.__build()

    @staticmethod
    def create_nomenclature():
        group=group_nomenclature_model.create_group()
        unit1=nomenclature_model('Мука пшеничная',unit_measurement_model.create_killogramm())
        unit2=nomenclature_model('Сахар',unit_measurement_model.create_killogramm())
        unit3=nomenclature_model('Сливочное масло',unit_measurement_model.create_killogramm())
        unit4=nomenclature_model('Яйца',unit_measurement_model.create_thing())
        unit5=nomenclature_model('Ванилин',unit_measurement_model.create_gramm())
        unit6=nomenclature_model('Куриное филе',unit_measurement_model.create_killogramm())
        unit7=nomenclature_model('Салат романо',unit_measurement_model.create_killogramm())
        unit8=nomenclature_model('Сыр Пармезан',unit_measurement_model.create_killogramm())
        unit9=nomenclature_model('Чеснок',unit_measurement_model.create_thing())
        unit10=nomenclature_model('Белый хлеб',unit_measurement_model.create_gramm())
        unit11=nomenclature_model('Соль',unit_measurement_model.create_killogramm())
        unit12=nomenclature_model('Черный перец',unit_measurement_model.create_gramm())
        unit13=nomenclature_model('Оливковое масло',unit_measurement_model.create_litr())
        unit14=nomenclature_model('Лимоновый сок',unit_measurement_model.create_mililitr())
        unit15=nomenclature_model('Горчица дижонская',unit_measurement_model.create_killogramm())
        unit16=nomenclature_model('Сахарная пудра',unit_measurement_model.create_killogramm())
        unit17=nomenclature_model('Корица',unit_measurement_model.create_gramm())
        unit18=nomenclature_model('Какао',unit_measurement_model.create_gramm())
        group.list_positions=[unit1,unit2,unit3,unit4,unit5,unit6,unit7,unit8,unit9,unit10,
                              unit11,unit12,unit13,unit14,unit15,unit16,unit17,unit18]
        return group
    
    @staticmethod
    def create_receipts():
        result = []
        data = start_factory.create_nomenclatures().list_positions
        
        # ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ
        items = {"Мука пшеничная": 100, "Сахар": 80, "Сливочное масло": 70, "Яйца": 1 , "Ванилин": 5 }
        item = receipe_model.create_receipt("ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ", "", items, data)
        
        # Шаги приготовления
        item.instructions.append("Масло положите в сотейник с толстым дном. Растопите его на маленьком огне на плите, на водяной бане либо в микроволновке.")
        item.instructions.append("Добавьте в теплое масло сахар. Перемешайте венчиком до полного растворения сахара. От тепла сахар довольно быстро растает.")
        item.instructions.append("Добавьте в масло яйцо. Предварительно все-таки проверьте масло, не горячее ли оно, иначе яйцо может свариться. Перемешайте яйцо с маслом до однородности.")
        item.instructions.append("Всыпьте муку, добавьте ванилин.")
        item.instructions.append("Перемешайте массу венчиком до состояния гладкого однородного теста.")
        
        item.comments = "Время приготовления: 20 мин. 8 порций"
        result.append( item )
        
        # Цезарь с курицей
        items =  {"Куриное филе": 200, "Салат Романо": 50, "Сыр Пармезан": 50,
                  "Чеснок": 10 , "Белый хлеб": 30 , "Соль": 5, "Черный перец": 2,
                  "Оливковое масло": 10, "Лимонный сок": 5, "Горчица дижонская": 5,
                  "Яйца": 2}
                
        item =  receipe_model.create_receipt("Цезарь с курицей", "", items, data)
        item.instructions.append("Нарезать куриное филе кубиками, нарубите чеснок, нарежьте хлеб на кубики.")
        item.instructions.append("Очистить салат и обсушить его.")
        item.instructions.append("Натереть сыр Пармезан на терке.")
        item.instructions.append("Обжарить на сковороде куриное филе с чесноком до готовности.")
        item.instructions.append("На той же сковородке обжарьить кубики хлеба до золотистости.")
        item.instructions.append("В миске смешайте оливковое масло, лимонный сок, горчицу, измельченный чеснок, соль и перец.")
        item.instructions.append("В большой миске смешайте кубики курицы, хлеба, листья салата.")
        item.instructions.append("Добавить заправку и тщательно перемешать")
        result.append(item)
        
        # Безе
        items = {"Яйца": 3, "Сахарная пудра":180, "Ванилиин" : 5, "Корица": 5 ,"Какао": 20} 
        result.append( receipe_model.create_receipt("Безе", "", items, data))
        return result


    def create(self):
        if self.__settings.is_first_start==True:
            self.__settings.is_first_start=False
            return start_factory.create_nomenclature()
        else:
            group=group_nomenclature_model.create_group()
            return group
        
    def __build(self):
        if self.__storage==None:
            self.__storage=storage()
        
        self.__storage.data[storage.nomenculature_key()]=self.create_nomenclature().list_positions
        self.__storage.data[storage.measurement_key()]=[i.unit_measurement for i in self.create_nomenclature().list_positions]
        self.__storage.data[storage.group_key()]=self.create_nomenclature()

    @property
    def storage(self):
        return self.__storage