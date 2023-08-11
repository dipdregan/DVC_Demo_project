from dataclasses import dataclass
import os
from pathlib import Path
import yaml
import pandas as pd

@dataclass(frozen= True)
def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

@dataclass
def save_data_as_csv(data, csv_path):
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
    print(f"Data saved as CSV: {csv_path}")