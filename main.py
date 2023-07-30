from src.mlflow_demo import logger
from src.mlflow_demo.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n')
except Exception as e:
    logger.exception(e)
    raise e