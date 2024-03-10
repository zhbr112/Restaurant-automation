from src.Logics.report.report_abstract import report_abstract
from src.Logics.start_factory import start_factory
from src.argument_exception import arguent_exception


class report_csv(report_abstract):
    __str_csv: str = ""

    def create(self, key: str):
        """
        Создание строки типа csv, с данными из storage
        """
        self.__str_csv= ""
        self.data = self.sdata.get(key)
        if self.data is None:
            raise arguent_exception("Таких данных несуществует")

        # Получение название столбцов
        names = (
            ";".join(
                [
                    unit.split("__")[1].capitalize().replace("_", " ")
                    for unit in vars(self.data[0]) if hasattr(self.data[0],unit.split("__")[1])
                ]
            )
            + "\n"
        )
        self.str_csv += names

        # Формирование строки csv
        for num_l, line in enumerate(self.data):
            for num_u, unit in enumerate(vars(line)):
                if hasattr(line,unit.split("__")[1]):
                    unit=getattr(line,unit.split("__")[1])
                    if "src." in str(type(unit)):
                        self.str_csv+=str(unit.id)+';'
                        continue

                    if isinstance(unit, list):
                        self.str_csv+=",".join([str(unit_in_list_unit.id) for unit_in_list_unit in unit])+';'
                        continue
                    
                    self.str_csv+=str(unit)+';'
            
            self.str_csv = self.str_csv[:-1] + "\n"
            
        return self.str_csv

    @property
    def str_csv(self):
        return self.__str_csv

    @str_csv.setter
    def str_csv(self, value):
        self.__str_csv = value
