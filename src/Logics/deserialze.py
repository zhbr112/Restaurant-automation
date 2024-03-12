import json
from src.Storage.storage import storage
from src.models.unit_measurement_model import unit_measurement_model

def open_():
    with open('json.json') as f:
        data=json.loads(f.read())
    return data

def deserialze():
    data=open_()
    storage_=storage()
    for i in data:
        model=deserialze_(i)
        storage_.data[storage.measurement_key()].append(model)

def deserialze_(model):
    q=unit_measurement_model.create_gramm()
    print([i.lower().replace(' ','_') for i in model.keys()])
    print(sorted([unit.split("__")[1] for unit in vars(q) if hasattr(q,unit.split("__")[1])]))

deserialze()