from flask import Flask
from src.settings_manager import settings_manager
from src.Logics.report_factory import report_factory
from src.Logics.start_factory import start_factory

app= Flask(__name__)

@app.route("/api/report/<storage_key>", methods=['GET'])
def get_report(storage_key:str):
    data=start_factory().storage.data
    settings=settings_manager().settings
    if storage_key in data.keys():
        report=report_factory()
        format=settings.report_form_types
        report.create(settings,format,data).create(storage_key)
        response_type=app.response_class(
        response=report.create(settings,format,data).create(storage_key),
        status=200,
        mimetype='application/text'
    )
    

    return response_type

if __name__=='__main__':
    app.run(debug=True)
