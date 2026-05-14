# Component - Data Ingestion

import urllib.request as request
from src.datascience import logger
import os
import zipfile
from src.datascience.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    # Download Zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists")
    
    # Extract Zip file
    def extract_zip(self):
        """
        Extracts the zip file into the data directory
        Function returns none
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as file:
            file.extractall(unzip_path) 