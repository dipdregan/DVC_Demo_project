from src.logger import logging
import pandas as pd

class MongoDataSource:
    def __init__(self, connection):
        self.client = connection
        self.db = None

    def fetch_records(self, collection):
        try:
            records = list(collection.find())
            return records
        except Exception as e:
            logging.info(f"Failed to Fetch the records: {e}")
            return []

    