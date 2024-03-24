from flask import Flask, request
from src.settings_manager import settings_manager
from src.Logics.report.report_factory import report_factory
from src.Logics.start_factory import start_factory
from src.argument_exception import arguent_exception
from datetime import datetime
from src.Storage.storage import storage
import json
from src.Storage.storage_service import storage_service
from src.models.storage_tranzaction import storage_tranzaction


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
def get_rests_date():
    args = request.args
    if ('start_period', 'stop_period') not in args.keys():
        arguent_exception('Необходимо передавать start_period, stop_period')
    
    start_date=datetime.strptime(args['start_period'], '%Y-%m-%d')
    stop_date=datetime.strptime(args['stop_period'], '%Y-%m-%d')

    rests=storage_service.create_turns_date(data[storage.jornal_key()],start_date,stop_date)

    result=storage_service.create_response(rests)

    return result

@app.route("/api/storage/<nomenclature_id>/turns", methods=["GET"])
def get_rests_nom(nomenclature_id: str):

    rests=storage_service.create_turns_nom(data[storage.jornal_key()], nomenclature_id)

    result=storage_service.create_response(rests)

    return result

@app.route("/api/storage/<receipt_name>/debits", methods=["GET"])
def get_rests(receipt_name: str):
    args = request.args
    if 'storage' not in args:
        raise arguent_exception("Не указан склад!")

    receipt = [recipe for recipe in start_factory().storage.data[storage.receipt_key()] if recipe.name == receipt_name][0]
    storage_ = [storage for storage in start_factory().storage.data[storage.storage_key()] if storage.name == args['storage']][0]

    rests=storage_service.create_turns_receipt(data[storage.jornal_key()], receipt, storage_)

    recipe_need = {}
    for recipe_row in receipt.rows:
        recipe_need[receipt.rows[recipe_row].nomenclature.full_name] = receipt.rows[recipe_row].size

    transactions = []
    for rest in rests:
        if recipe_need[rest.nomenclature.full_name] > rest.turn:
            raise arguent_exception('Не удалось произвести списование! Остатков на складе не достаточно!')
        transactions.append(storage_tranzaction().create(storage_, rest.nomenclature, -recipe_need[rest.nomenclature.full_name], rest.unit_measurement, period=datetime.now()))

    start_factory().storage.data[storage.jornal_key()] += transactions

    return app.response_class(
            response = json.dumps({'success': True}),
            status=200,
            mimetype="application/json; charset=utf-8"
        )


if __name__ == "__main__":
    app.run(debug=True)
