from src.logger import logging
from src.mongo_db.Mongo_connection import MongoDBConnection
from src.mongo_db.mongo_data_source import MongoDataSource
from src.utils.utlis import read_params
import os
import pandas as pd



def data_loading_mongodb():
    try:
        logging.info(f"{'=='*10} Pipeline Grabbing data from MongoDB started...{'=='*10}")
        logging.info(f"{'=='*30}")
        config_path = os.path.join(os.getcwd(), "params.yaml")
        params = read_params(config_path)
        mongo = params['data_source']['mongo_db']
        path = params['load_data']['raw_dataset_csv']

        logging.info(f"{'=='*10} connection started..... {'=='*10}")
        
        connection = MongoDBConnection(
            host=mongo['host'],
            port=mongo['port']
        )
        client = connection.connect()

        logging.info(f"{'=='*10} Connection Stablished...{'=='*10}")

        data_source = MongoDataSource(client)
        collection = mongo['collection_name']
        database = mongo['db_name']
        logging.info(f"{'=='*10} Fetching the record...{'=='*10}")

        data = data_source.fetch_records(database,collection)
        df = pd.DataFrame(data)
        new_cols = [col.replace(" ", "_") for col in df.columns]
        df.columns = new_cols
        
        df.to_csv(path, sep=',', index=False) 

        logging.info(f"{'=='*10} Saved the record to ...{path} this path {'=='*10}")
        logging.info(f"{'=='*50}")

    except Exception as e:
        logging.error(str(e))

if __name__ == "__main__":
    data_loading_mongodb()
