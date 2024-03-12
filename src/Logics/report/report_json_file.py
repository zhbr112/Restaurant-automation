from src.Logics.start_factory import start_factory
from src.settings_manager import settings_manager
from src.Logics.report.report_json import report_json
from src.Storage.storage import storage



data = start_factory().storage.data
settings=settings_manager().settings
report_csv_=report_json(settings,data)
data=report_csv_.create(storage.measurement_key())
with open('json.json','w') as f:
    f.write(data)