from src.settings_manager import settings_manager
from src.Logics.start_factory import start_factory


class report:
    __manager = settings_manager()
    __data=None

    def __init__(self, data):
        storage=start_factory().storage
        dat=storage.data[data]
        # dat=self.manager.settings
        self.__data=dat
        
        match self.manager.settings.report_form_types:
            case "CSV":
                self.report_csv(data)
            case "Markdown":
                self.report_mkd(data)
            case "Json":
                self.report_json(data)

    def report_csv(self, data):
        with open(f"Reports/report_{data}.csv",'w') as file:
            names=';'.join([j.split("__")[1].capitalize().replace('_',' ') for j in vars(self.data[0])])
            file.write(names+'\n')
            for i in self.data:
                dat=[]
                for j in vars(i).values():
                    if 'src.' in str(type(j)):
                        dat.append(str(j.id))
                        continue
                    if isinstance(j,list):
                        for k in j:
                           dat.append(str(k.id)) 
                        continue
                    dat.append(str(j))
                file.write(';'.join(dat)+'\n')
    @property
    def manager(self):
        return self.__manager

    @property
    def pole(self):
        return self.__pole
    
    @property
    def data(self):
        return self.__data