import os
from src.mlflow_demo import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.mlflow_demo.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    ## Note: We can add different data transformation techniques as PCA, Scaler and so on.
    def train_test_spliting(self):
        df = pd.read_csv(self.config.data_path)
        train, test = train_test_split(df)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info('Splited data into train and test arrays')
        logger.info(f'Train shape {train.shape}')
        logger.info(f'Test shape {test.shape}')

        print(f'Train shape {train.shape}')
        print(f'Test shape {test.shape}')
