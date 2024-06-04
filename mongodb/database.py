from pymongo import MongoClient


DATABASE_URL = 'mongodb://localhost:27017/'
DATABASE_NAME = 'bank'

class Database:
    
    def __init__(self, uri: str = DATABASE_URL, db_name: str = DATABASE_NAME):
        
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.clientes_collection = self.db['cliente']