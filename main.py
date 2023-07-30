from src.mlflow_demo import logger
from src.mlflow_demo.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlflow_demo.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

INGESTION_STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f'>>>>> Stage {INGESTION_STAGE_NAME} started <<<<<')
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f'>>>>> Stage {INGESTION_STAGE_NAME} completed <<<<<\n\n')
except Exception as e:
    logger.exception(e)
    raise e

VALIDATION_STAGE_NAME = 'Data Validation stage'

try:
    logger.info(f'>>>>> Stage {VALIDATION_STAGE_NAME} started <<<<<')
    pipeline = DataValidationTrainingPipeline()
    pipeline.main()
    logger.info(f'>>>>> Stage {VALIDATION_STAGE_NAME} completed <<<<<\n\n')
except Exception as e:
    logger.exception(e)
    raise e