from src.logger import logging
import pandas as pd

class MongoDataSource:
    def __init__(self, connection):
        self.client = connection
        self.db = None

    def fetch_records(self, database_name,collection_name):
        try:
            db = self.client.get_database(database_name)
            collection = db[collection_name]

            projection = {'_id': 0}

            records = list(collection.find({}, projection))
            logging.info(records)
            return records

        except Exception as e:
            logging.info(f"Failed to Fetch the records: {e}")
            return []

    