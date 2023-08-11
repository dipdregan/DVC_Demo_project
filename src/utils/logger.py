import logging
import os
from datetime import datetime


LOG_FILE = F"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FOLDER = 'log'
log_path = os.path.join(os.getcwd(),LOG_FOLDER,LOG_FILE)

os.makedirs(log_path,exist_ok= True)

LOG_FILE_PATH= os.path.join(log_path, LOG_FILE)

logging.info(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)