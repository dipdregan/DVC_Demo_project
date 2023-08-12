import yaml
import pandas as pd
from src.logger import logging

def read_params(config_path):
    try:
        logging.info("reading the file...........")
        with open(config_path) as yaml_file:
            config = yaml.safe_load(yaml_file)
            logging.info(f"yaml file read \n{config}")
        return config
    except Exception as e:
        logging.info(str(e))

def export_to_csv(data, csv_filename):
    try:
        df = pd.DataFrame(data)
        df.to_csv(csv_filename, index=False)
        logging.info(f"Data exported to {csv_filename}")
    except Exception as e:
        logging.error(f"Failed to export data to CSV: {e}")