from src.models.storage_turn_model import storage_turn_model


class process_storage_turn:
    @classmethod
    def create(self, transactions):
        res = {}
        for t in transactions:
            conversion=1            
            while(t.unit_measurement.basic_unit_measurement is not None):
                conversion*=t.unit_measurement.conversion_factor
                t.unit_measurement=t.unit_measurement.basic_unit_measurement

            key = (t.storage, t.nomenclature, t.unit_measurement)
            value = t.count*conversion
            if key in res.keys():
                res[key] += value
            else:
                res[key] = value

        result = []
        for key, value in res.items():
            t = storage_turn_model.create(key[0],key[1],value,key[2])
            result.append(t)
        return result
