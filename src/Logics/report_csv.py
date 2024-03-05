from src.Logics.report_abstract import report_abstract
from src.Logics.start_factory import start_factory
from src.argument_exception import arguent_exception


class report_csv(report_abstract):
    __str_csv: str = ""

    def create(self, key: str):
        """
        Создание строки типа csv, с данными из storage
        """
        storage = start_factory().storage
        self.data = storage.data.get(key)
        if self.data is None:
            raise arguent_exception("Таких данных несуществует")

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
        lines = [[] for line in self.data]
        for num_l, line in enumerate(self.data):
            for num_u, unit in enumerate(vars(line).values()):
                if "src." in str(type(unit)):
                    lines[num_l].append(str(unit.id))
                    continue

                if isinstance(unit, list):
                    lines[num_l].append(
                        ",".join(
                            [str(unit_in_list_unit.id) for unit_in_list_unit in unit]
                        )
                    )
                    continue
                lines[num_l].append(str(unit))
            self.str_csv += ";".join(lines[num_l]) + "\n"
        return self.str_csv

    @property
    def str_csv(self):
        return self.__str_csv

    @str_csv.setter
    def str_csv(self, value):
        self.__str_csv = value