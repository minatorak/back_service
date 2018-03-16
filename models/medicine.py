import uuid

from common.database import Database


class Medicine(object):
    def __init__(self, name, type_medicine, medicine_for,
                 medicine_facts, medicine_use,
                 medicine_risk, medicine_store, _id=None):
        self.name = name
        self.type_medicine = type_medicine
        self.medicine_for = medicine_for
        self.medicine_facts = medicine_facts
        self.medicine_use = medicine_use
        self.medicine_risk = medicine_risk
        self.medicine_store = medicine_store
        self._id = uuid.uuid4().hex if _id is None else _id


    @staticmethod
    def new_medicine(name,
                     type_medicine,
                     medicine_for,
                     medicine_facts,
                     medicine_use,
                     medicine_risk,
                     medicine_store):

        medicine = Medicine(name,type_medicine,
                            medicine_for,
                            medicine_facts,
                            medicine_use,
                            medicine_risk,
                            medicine_store)
        medicine.save_to_mongo()

    def save_to_mongo(self):
        Database.insert(collection='medicine',
                        data=self.json())

    def json(self):
        return {
            'name': self.name,
            'type_medicine': self.type_medicine,
            'medicine_for': self.medicine_for,
            'medicine_facts': self.medicine_facts,
            'medicine_use': self.medicine_use,
            'medicine_risk': self.medicine_risk,
            'medicine_store': self.medicine_store
        }

    @classmethod
    def from_mongo(cls):
        return [medicine for medicine in Database.find_all('medicine')]

    @staticmethod
    def re_data(data):
        return {
            'name': data['name'],
            'type_medicine': data['type_medicine'],
            'medicine_for': data['medicine_for'],
            'medicine_facts': data['medicine_facts'],
            'medicine_use': data['medicine_use'],
            'medicine_risk': data['medicine_risk'],
            'medicine_store': data['medicine_store']
        }
