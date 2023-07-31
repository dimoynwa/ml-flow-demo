from src.mlflow_demo.config.configuration import ConfigurationManager
from src.mlflow_demo import logger
from src.mlflow_demo.components.data_transformation import DataTransformation
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'), 'r') as f:
                status = f.read().split(" ")[-1]
            
            if status == "True":
                config_manager = ConfigurationManager()
                config = config_manager.get_data_transformation_config()
                data_transformation = DataTransformation(config=config)
                data_transformation.train_test_spliting()
            else:
                logger.error('The data is NOT VALID')
                raise Exception("Data NOT VALID")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
        pipeline = DataTransformationTrainingPipeline()
        pipeline.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n')
    except Exception as e:
        logger.exception(e)
        raise e