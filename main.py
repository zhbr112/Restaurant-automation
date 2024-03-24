from flask import Flask, request
from src.settings_manager import settings_manager
from src.Logics.report.report_factory import report_factory
from src.Logics.start_factory import start_factory
from src.argument_exception import arguent_exception
from datetime import datetime
from src.Storage.storage import storage
import json
from src.Storage.storage_service import storage_service


app = Flask(__name__)

data = start_factory().storage.data
report = report_factory()
settings = settings_manager().settings
format = settings.report_form_types

@app.route("/api/report/<storage_key>", methods=["GET"])
def get_report(storage_key: str):      
    if storage_key in data.keys():
        report.create(settings, format, data).create(storage_key)
        if settings.report_form_types == "json":
            response_type = app.response_class(
                response=report.create(settings, format, data).create(storage_key),
                status=200,
                mimetype="application/json; charset=utf-8",
            )
        else:
            response_type = app.response_class(
                response=report.create(settings, format, data).create(storage_key),
                status=200,
                mimetype="application/text",
            )
    else:
        response_type = app.response_class(
            response="Внутреняя ошибка сервера", status=500
        )

    return response_type

@app.route("/api/storage/rests", methods=["GET"])
def get_rests():
    args = request.args
    if ('start_period', 'stop_period') not in args.keys():
        arguent_exception('Необходимо передавать start_period, stop_period')
    
    start_date=datetime.strptime(args['start_period'], '%Y-%m-%d')
    stop_date=datetime.strptime(args['stop_period'], '%Y-%m-%d')

    rests_data=storage_service.create_turns(data[storage.jornal_key()],start_date,stop_date)

    result=storage_service.create_response(rests_data)

    return result


if __name__ == "__main__":
    app.run(debug=True)
