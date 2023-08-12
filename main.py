from src.mongo_db.mongo_connection import MongoDBConnection
from src.mongo_db.mongo_db_operation import MongoDBOperation
from src.mongo_db.mongo_data_source import M
from src.utils.utlis import read_params,save_data_as_csv
from src.logger import logging
import os

def main():
    try:
        # Read parameters from the config file
        config_path = os.path.join(os.getcwd(), "params.yaml")
        params = read_params(config_path)
        
        # Initialize MongoDB connection
        mongo_conn = MongoDBConnection(
            host=params['data_source']['mongo_db']['host'],
            port=params['data_source']['mongo_db']['port'],
            username=params['data_source']['mongo_db']['username'],
            password=params['data_source']['mongo_db']['password']
        )
        client = mongo_conn.connect()

        # Initialize MongoDB operation
        mongo_operation = MongoDBOperation(client)
        
        # Create a database and a collection
        db_name = params['data_source']['mongo_db']['db_name']
        collection_name = params['data_source']['mongo_db']['collection_name']
        db = mongo_operation.create_database(db_name)
        collection = mongo_operation.create_collection(db, collection_name)
        
        # Insert CSV data into the collection
        csv_path = params['load_data']['raw_dataset_csv']
        mongo_operation.insert_csv_data(collection, csv_path)
        logging.info("CSV data inserted into MongoDB")

        # Initialize MongoDB data source
        mongo_data_source = MongoDBDataSource(params)
        
        # Fetch data from MongoDB
        data = mongo_data_source.fetch_data_from_mongodb()
        for record in data:
            logging.info(record)

    except Exception as e:
        logging.error(str(e))

if __name__ == "__main__":
    main()
