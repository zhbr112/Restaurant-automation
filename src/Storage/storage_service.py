from src.argument_exception import arguent_exception
from datetime import datetime
from src.argument_exception import arguent_exception
from src.Logics.process_factory import process_factory
from src.Storage.storage import storage
from src.Logics.report.convertor.convert_factory import convert_factory
from src.Storage.storage_prototype import storage_prototype
from src.settings_manager import settings_manager
from flask import Flask, request
import json


class storage_service:
    __data=[]
    __convert=None
    __process=None

    @staticmethod
    def create_turns_date(data, start_period:datetime, stop_period:datetime):

        if start_period>stop_period:
            raise arguent_exception("Некорректно переданы параметры!")
        prototype=storage_prototype(data)
        transactions=prototype.filter_date(start_period,stop_period)
        processing =process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions)

        return rests
    
    @staticmethod
    def create_turns_nom(data, nom):
        prototype=storage_prototype(data)
        transactions=prototype.filter_nom(nom)
        processing =process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions)

        return rests
    
    @staticmethod
    def create_turns_receipt(data, receipt, storage_):
        prototype=storage_prototype(data)
        prototype.filter_receipt(receipt)
        transactions=prototype.filter_storage(storage_.id)
        processing = process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions)

        return rests
    
    @staticmethod
    def create_response(data):
        app = Flask(__name__)
        rests_data = convert_factory().convert_obj(data)
        json_data=(json.dumps(rests_data, indent=4, ensure_ascii=False))
        response_type = app.response_class(
            response=json_data,
            status=200,
            mimetype="application/json; charset=utf-8"
            )
        return response_type
        
