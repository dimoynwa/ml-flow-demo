from src.mlflow_demo.constants import *
from src.mlflow_demo.utils.common import read_yaml, create_directories
from src.mlflow_demo.entity.config_entity import (DataIngestionConfig,
                                                  DataValidationConfig,
                                                  DataTransformationConfig,
                                                  ModelTrainerConfig)

class ConfigurationManager:
    def __init__(self, 
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH) -> None:
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        create_directories([self.config.data_ingestion.root_dir])
        return DataIngestionConfig(
            root_dir=self.config.data_ingestion.root_dir,
            source_URL=self.config.data_ingestion.source_URL,
            local_data_file=self.config.data_ingestion.local_data_file,
            unzip_dir=self.config.data_ingestion.unzip_dir
        )
    
    def get_data_validation_config(self) -> DataValidationConfig:
        create_directories([self.config.data_validation.root_dir])
        return DataValidationConfig(
            root_dir=self.config.data_validation.root_dir,
            unzip_data_dir=self.config.data_validation.unzip_data_dir,
            STATUS_FILE=self.config.data_validation.STATUS_FILE,
            all_schema=self.schema.COLUMNS
        )
    
    def get_data_transformation_config(self):
        create_directories([self.config.data_transformation.root_dir])
        return DataTransformationConfig(root_dir=self.config.data_transformation.root_dir,
                                        data_path=self.config.data_transformation.data_path)
    

    def get_model_trainer_config(self):
        create_directories([self.config.model_trainer.root_dir])
        return ModelTrainerConfig(root_dir=self.config.model_trainer.root_dir,
                                  train_data_path=self.config.model_trainer.train_data_path,
                                  test_data_path=self.config.model_trainer.test_data_path,
                                  model_name= self.config.model_trainer.model_name,
                                  alpha=self.params.ElasticNet.alpha,
                                  l1_ratio=self.params.ElasticNet.l1_ratio,
                                  target_column=self.schema.TARGET_COLUMN.name)
    