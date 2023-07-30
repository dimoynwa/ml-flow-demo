from src.mlflow_demo import logger
from src.mlflow_demo.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        self.config = config

    def validate_all_columns(self) -> bool:
        validation_status = None
        
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            missing_columns = [col for col in all_cols if not col in all_schema]

            validation_status = True if len(missing_columns) == 0 else False

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f'Validation status: {validation_status}')

            return validation_status
        except Exception as e:
            logger.exception(e)
            raise e