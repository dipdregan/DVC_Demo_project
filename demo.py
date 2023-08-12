from src.pipeline.Stage01_data_ingetion_pipeline import data_ingestion_mongodb
from src.pipeline.Stage02_grabing_data_from_mongo_pipeline import data_loading_mongodb

if __name__ == "__main__":
    data_loading_mongodb()
