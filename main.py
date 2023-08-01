from src.mlflow_demo import logger
from src.mlflow_demo.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlflow_demo.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlflow_demo.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.mlflow_demo.pipeline.stage_04_model_trainer import ModelTrainTrainingPipeline
from src.mlflow_demo.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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

TRANSFORMATION_STAGE_NAME = 'Data Transformation stage'
try:
    logger.info(f'>>>>> Stage {TRANSFORMATION_STAGE_NAME} started <<<<<')
    pipeline = DataTransformationTrainingPipeline()
    pipeline.main()
    logger.info(f'>>>>> Stage {TRANSFORMATION_STAGE_NAME} completed <<<<<\n\n')
except Exception as e:
    logger.exception(e)
    raise e

MODEL_TRAIN_STAGE_NAME = 'Model train stage'
try:
    logger.info(f'>>>>> Stage {MODEL_TRAIN_STAGE_NAME} started <<<<<')
    pipeline = ModelTrainTrainingPipeline()
    pipeline.main()
    logger.info(f'>>>>> Stage {MODEL_TRAIN_STAGE_NAME} completed <<<<<\n\n')
except Exception as e:
    logger.exception(e)
    raise e

MODEL_EVAL_STAGE_NAME = 'Model evaluation stage'
try:
    logger.info(f'>>>>> Stage {MODEL_EVAL_STAGE_NAME} started <<<<<')
    pipeline = ModelEvaluationTrainingPipeline()
    pipeline.main()
    logger.info(f'>>>>> Stage {MODEL_EVAL_STAGE_NAME} completed <<<<<\n\n')
except Exception as e:
    logger.exception(e)
    raise e