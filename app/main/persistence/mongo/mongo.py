import json
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from uuid import UUID


import settings
from app.main.utils.singleton import Singleton


class MongoDB(object):

    def __init__(self):
        self._databse = settings.MONGO_DATABASE
        self.conn = self.get_instance

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()

    @property
    def connection_database(self):
        return MongoClient("mongodb+srv://cedrotech_ai:tEnrrKgE@cluster0-h1dgk.gcp.mongodb.net/machine-learning?retryWrites=true&w=majority")

    @property
    def get_instance(self):
        rw = Singleton()
        rw.conn = self.connection_database
        return rw.conn

    def test_ping(self):
        x = self.conn[self._databse].command('ping')
        return x.get('ok', '')

    def save_one(self, obj, collection) -> str:
        db = self.conn[self._databse]
        x = db[collection].insert_one(obj)
        return x.inserted_id

    def save_list(self, obj_list, collection) -> list:
        db = self.conn[self._databse]
        x = db[collection].insert_many(obj_list)
        return x.inserted_ids

    def find_all(self, collection, **kwargs) -> list:
        data = []
        db = self.conn[self._databse]
        x = db[collection].find(kwargs)
        for row in x:
            data.append(row)
        return json.loads(json.dumps(data, default=MongoDB.new_encoder))

    def find_one(self, collection, **kwargs) -> object:
        db = self.conn[self._databse]
        x = db[collection].find_one(kwargs)
        return x

    def find_all_aggregation(self, collection, from_collection, local_field, foreign_field, new_name_key) -> list:
        data = []
        db = self.conn[self._databse]

        x = db[collection].aggregate(
            [
                {
                    "$lookup": {
                        "from": from_collection,
                        "localField": local_field,
                        "foreignField": foreign_field,
                        "as": new_name_key
                    }
                },
                {'$limit': 1}
            ]
        )
        for row in x:
            data.append(row)
        return json.loads(json.dumps(data, default=MongoDB.new_encoder))

    def check_exists_collection(self, collection):
        db = self.conn[self._databse]
        return db[collection]

    def drop_collection(self, collection):
        db = self.conn[self._databse]
        db[collection].drop()

    def close_connection(self):
        self.conn.close()

    @staticmethod
    def new_encoder(o):
        if type(o) in (ObjectId, UUID):
            return str(o)
        elif type(o) == datetime:
            return o.isoformat()
        return o
