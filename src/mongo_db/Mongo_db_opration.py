import pandas as pd
from src.mongo_db.Mongo_connection import MongoDBConnection
from src.logger import logging


class MongoDBOperation:

    def __init__(self, connection):
        self.client = connection
        self.db = None
    
    def create_database(self,db_name):
        try:
            if db_name in self.client.list_database_names():
                logging.info(f"Database '{db_name}' already exists..(; ")
                return self.client[db_name]
            else:
                db = self.client[db_name]

                logging.info(f"Database '{db_name}' created successfully....")
                return db
        except Exception as e:
            logging.info(f"Failed to create database : {e}")
            return None
        
    def create_collection(self, db, collection_name):
        try:
            if collection_name in db.list_collection_names():
                logging.info(f"Collection '{collection_name}' already exists....")
                return db[collection_name]
            
            else:
                collection = db[collection_name]
                logging.info(f"Collection '{collection_name}' created successfully......")
                return collection

        except Exception as e:
            logging.info(f"Failed to create collection: {e}")
            return None
        
    def insert_single_record(self, collection, record):
        try:
            inserted_id = collection.insert_one(record).inserted_id
            logging.info(f"Record inserted with ID: {inserted_id}")
            return inserted_id

        except Exception as e:
            logging.info(f"Failed to insert record : {e}")
            return None
        
    def insert_csv_data(self, collection, csv_path):
        try:
            df = pd.read_csv(csv_path)
            data = df.to_dict(orient='records')

            result = collection.insert_many(data)
            logging.info(f"{len(result.inserted_ids)} documents inserted successfully...(;")
            
        except Exception as e:
            logging.info(f"Failed to insert CSV data : {e}")

    def fetch_record(self, collection):
        try:
            records = list(collection.find())
            for record in records:
                print(record)
                logging.info(record)

        except Exception as e:
            logging.info(f"Failed to Fetch the records: {e}")

    def list_databases(self):
        try:
            databases = self.client.list_database_names()
            for db_name in databases:
                logging.info(f"The list of databases are :-\n{'=='*20}")
                logging.info(db_name)
                logging.info(f"{'=='*20}")
        except Exception as e:
            logging.info(f"Failed to list databases: {e}")

    def delete_database(self, db_name):
        try:
            self.client.drop_database(db_name)
            logging.info(f"Database '{db_name}' deleted successfully...")
        except Exception as e:
            logging.info({str(e)})

    def delete_all_database(self):
        try:
            db_names = self.client.list_database_names()
            for name in db_names:
                if name not in ['admin', 'config', 'local']:
                    self.client.drop_database(name)
                    logging.info(f"Database '{name}' deleted successfully...")
        except Exception as e:
            logging.info(f"Failed to delete databases: {e}")
