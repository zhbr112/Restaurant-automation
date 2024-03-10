from src.Logics.report.report_abstract import report_abstract
from src.Logics.start_factory import start_factory
from src.argument_exception import arguent_exception


class report_mardown(report_abstract):
    __str_md: str = ""

    def create(self, key: str):
        """
        Создание строки типа md, с данными из storage
        """
        self.__str_md= ""
        self.data = self.sdata.get(key)
        if self.data is None:
            raise arguent_exception("Таких данных несуществует")

        # Получение название столбцов
        names = '|'+(
            "|".join(
                [
                    unit.split("__")[1].capitalize().replace("_", " ")
                    for unit in vars(self.data[0])
                ]
            )
            + "|\n"
        )
        self.str_md += names
        self.str_md+='|'+'|'.join(['-' for _ in range(names.count('|')-1)])+'|\n'

        # Формирование строки md
        for num_l, line in enumerate(self.data):
            for num_u, unit in enumerate(vars(line).values()):
                if "src." in str(type(unit)):
                    self.str_md+='|'+str(unit.id)
                    continue

                if isinstance(unit, list):
                    self.str_md+='|'+",".join([str(unit_in_list_unit.id) for unit_in_list_unit in unit])
                    continue
                
                self.str_md+='|'+str(unit)
            
            self.str_md = self.str_md + "|\n"
        s=self.str_md.split('\n')

        return self.str_md

    @property
    def str_md(self):
        return self.__str_md

    @str_md.setter
    def str_md(self, value):
        self.__str_md = value
