from src.mlflow_demo.config.configuration import ConfigurationManager
from src.mlflow_demo import logger
from src.mlflow_demo.components.model_trainer import ModelTrainer
from pathlib import Path

STAGE_NAME = "Model train stage"

class ModelTrainTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_manager = ConfigurationManager()
        config = config_manager.get_model_trainer_config()
        data_transformation = ModelTrainer(config=config)
        data_transformation.train()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
        pipeline = ModelTrainTrainingPipeline()
        pipeline.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n')
    except Exception as e:
        logger.exception(e)
        raise e