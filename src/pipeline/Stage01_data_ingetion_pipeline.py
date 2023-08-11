from src.mongo_db.Mongo_db_opration import MongoDBConnection
from src.mongo_db.Mongo_db_opration import MongoDBOperation
from src.utils.utlis import read_params
from src.logger import logging
import os


def data_ingestion_mongodb():
    try:
        # Read parameters from the config file
        config_path = os.path.join(os.getcwd(), "params.yaml")
        params = read_params(config_path)
        mongo = params['data_source']['mongo_db']
        
        # Initialize MongoDB connection
        connection = MongoDBConnection(
                host=mongo['host'],
                port=mongo['port']
            )

        client = connection.connect()

        # Initialize MongoDB operation
        mongo_operation = MongoDBOperation(client)
        
        # Create a database and a collection
        db_name = mongo['db_name']
        collection_name = mongo['collection_name']
        db = mongo_operation.create_database(db_name)
        logging.info("==="*30)
        logging.info(f"Database {db_name} Created Successfully.....")
        logging.info("==="*30)

        collection = mongo_operation.create_collection(db, collection_name)
        logging.info("==="*30)
        logging.info(f"Collection {collection} created inside the database {db_name}...")
        logging.info("==="*30)

        data_path = r"F:\DVC\DVC_Demo_project\data_given\winequality.csv"
        data_insert = mongo_operation.insert_csv_data(collection=collection,csv_path=data_path)
        
        logging.info("==="*30)
        logging.info(f"Data inserted into MongoDB database in'{db_name}' and in collection '{collection_name}'")
        logging.info("==="*30)
        logging.info(data_insert)

    except Exception as e:
        logging.error(str(e))
