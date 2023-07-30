import os
import zipfile
from pathlib import Path
from src.mlflow_demo import logger
import urllib.request as req
from src.mlflow_demo.utils.common import get_size
from src.mlflow_demo.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = req.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logger.info(f'File {filename} downloaded with info {headers}')
        else:
            logger.info(f'File {self.config.local_data_file} already exists with size {get_size(Path(self.config.local_data_file))}')
            
    def extract_zip_file(self):
        os.makedirs(self.config.unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip:
            zip.extractall(self.config.unzip_dir)
