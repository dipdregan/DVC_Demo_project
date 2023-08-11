from src.logger import logging
from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, host='localhost', port=27017, username=None, password=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = None

    def connect(self):
        try:
            if self.username and self.password:
                url = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}"
                self.client = MongoClient(url)
            else:
                self.client = MongoClient(self.host, self.port)
            logging.info("Connected to MongoDB....")
            return self.client
        except Exception as e:
            logging.info(f"Failed to connect to MongoDB: {e}")
