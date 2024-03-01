from src.Logics.report_abstract import report_abstract
from src.Logics.start_factory import start_factory
from typing import Iterator


class report_csv(report_abstract):
    __str_csv:str = ""

    def create(self, data:str):
        """
            Создание строки типа csv, с данными из storage
        """
        storage = start_factory().storage
        self.data = storage.data[data]

        # Получение название столбцов
        names = (
            ";".join(
                [
                    unit.split("__")[1].capitalize().replace("_", " ")
                    for unit in vars(self.data[0])
                ]
            )
            + "\n"
        )
        self.str_csv += names

        # Формирование строки csv
        for line in self.data:
            lines = []

            for unit in vars(line).values():
                if "src." in str(type(unit)):
                    lines.append(str(unit.id))
                    continue

                if isinstance(unit, Iterator):
                    for unit_in_list_unit in unit:
                        lines.append(str(unit_in_list_unit.id))
                    continue

                lines.append(str(unit))
            self.str_csv += ";".join(lines) + "\n"
        return self.str_csv

    @property
    def str_csv(self):
        return self.__str_csv

    @str_csv.setter
    def str_csv(self, value):
        self.__str_csv = value