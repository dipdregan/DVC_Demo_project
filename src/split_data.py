from src.logger import logging
from  src.utils.utlis import read_params
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def split_and_saved_data(config_path):
    
    
    config = read_params(config_path)
    test_data_path = config['split_data']['test_path']
    train_data_path = config['split_data']['train_path']
    split_ratio = config['split_data']['test_size']
    random_state = config['base']['random_state']
    raw_data_path = config['load_data']['raw_dataset_csv']

    df = pd.read_csv(raw_data_path)
    train, test = train_test_split(df,
                                   test_size=split_ratio,
                                   random_state=random_state
                                   )
    train.to_csv(train_data_path, index = False)
    test.to_csv(test_data_path, index = False)

if __name__ == "__main__":
    config_path = os.path.join(os.getcwd(),'params.yaml')
    split_and_saved_data(config_path)