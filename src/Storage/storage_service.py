from src.argument_exception import arguent_exception
from datetime import datetime
from src.argument_exception import arguent_exception
from src.Logics.process_factory import process_factory
from src.Storage.storage import storage
from src.Logics.report.convertor.convert_factory import convert_factory
from src.Storage.storage_prototype import storage_prototype
from src.settings_manager import settings_manager
from flask import Flask, request
from src.Logics.start_factory import start_factory
from src.models.storage_tranzaction import storage_tranzaction
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
        rests = processing.create(transactions.data)

        return rests
    
    @staticmethod
    def create_turns_nom(data, nom):
        prototype=storage_prototype(data)
        transactions=prototype.filter_nom(nom)
        processing =process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions.data)

        return rests
    
    @staticmethod
    def create_turns_receipt(data, receipt_id, storages):
        receipt = storage_service.search_receipt(receipt_id)
        storage_ = storage_service.search_storage(storages)
        prototype=storage_prototype(data)
        transactions=prototype.filter_storage(storage_.name).filter_receipt(receipt)
        processing = process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions.data)

        return rests
    
    @staticmethod
    def create_grad(rests, receipt_id, storages):
        receipt = storage_service.search_receipt(receipt_id)
        storage_ = storage_service.search_storage(storages)
        recipe_need = {}
        for recipe_row in receipt.rows:
            recipe_need[receipt.rows[recipe_row].nomenclature.full_name] = receipt.rows[recipe_row].size

        transactions = []
        for rest in rests:
            print(recipe_need[rest.nomenclature.full_name], rest.turn)
            if recipe_need[rest.nomenclature.full_name] > rest.turn:
                raise arguent_exception('Не удалось произвести списование! Остатков на складе не достаточно!')
            transactions.append(storage_tranzaction().create(storage_, rest.nomenclature, -recipe_need[rest.nomenclature.full_name], rest.unit_measurement, period=datetime.now()))

        return start_factory().storage.data[storage.jornal_key()] + transactions
    
    @staticmethod
    def search_receipt(receipt_id):
        receipt = [recipe for recipe in start_factory().storage.data[storage.receipt_key()] if recipe.id == receipt_id][0]
        if receipt is None:
            raise arguent_exception('Не верно переданы параметры')
        return receipt
        
    @staticmethod
    def search_storage(storages):
        storage_ = [storage for storage in start_factory().storage.data[storage.storage_key()] if storage.name == storages][0]
        if storage_ is None:
            raise arguent_exception('Не верно переданы параметры')
        return storage_
        
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
        
