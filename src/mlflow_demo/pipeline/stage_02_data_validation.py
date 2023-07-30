from src.mlflow_demo.config.configuration import ConfigurationManager
from src.mlflow_demo import logger
from src.mlflow_demo.components.data_validation import DataValidation

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_manager = ConfigurationManager()
        config = config_manager.get_data_validation_config()
        data_validation = DataValidation(config=config)
        validation_result = data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
        pipeline = DataValidationTrainingPipeline()
        pipeline.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n')
    except Exception as e:
        logger.exception(e)
        raise e