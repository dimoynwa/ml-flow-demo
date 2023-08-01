from pathlib import Path
from src.mlflow_demo.config.configuration import ConfigurationManager
from src.mlflow_demo import logger
from src.mlflow_demo.components.model_evaluation import ModelEvaluation


STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_manager = ConfigurationManager()
        config = config_manager.get_model_evaluation_config()
        data_transformation = ModelEvaluation(config=config)
        data_transformation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
        pipeline = ModelEvaluationTrainingPipeline()
        pipeline.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n')
    except Exception as e:
        logger.exception(e)
        raise e