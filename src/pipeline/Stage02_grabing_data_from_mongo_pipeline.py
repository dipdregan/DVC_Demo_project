from src.mongo_db.Mongo_connection import MongoDBConnection
from src.mongo_db.mongo_data_source import MongoDataSource
from src.utils.utlis import read_params, save_data_as_csv
from src.logger import logging
import os



def data_loading_mongodb():
    try:
        # Read parameters from the config file
        config_path = os.path.join(os.getcwd(), "params.yaml")
        params = read_params(config_path)
        mongo = params['data_source']['mongo_db']
        path = params['load_data']['raw_dataset_csv']
        
        # Initialize MongoDB connection
        connection = MongoDBConnection(
                host=mongo['host'],
                port=mongo['port']
            )

        client = connection.connect()

        # Initialize MongoDB DataSource
        data_source= MongoDataSource(client)

        collection = mongo['collection_name']
        data = data_source.fetch_records(collection)
        data_source.export_to_csv(data,path)


    except Exception as e:
        logging.info(str(e))