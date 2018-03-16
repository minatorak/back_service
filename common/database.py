import pymongo
class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['backservice']


    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find_all(type):
        if type == "medicine":
            db = Database.DATABASE.medicine
            return db.find()
        if type == "disease":
            db = Database.DATABASE.disease
            return db.find()
        return None
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)


    @staticmethod
    def dropCollection(collection):
        Database.DATABASE[collection].drop()