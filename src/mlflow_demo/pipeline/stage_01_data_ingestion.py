from src.mlflow_demo.config.configuration import ConfigurationManager
from src.mlflow_demo import logger
from src.mlflow_demo.components.data_ingestion import DataIngestion


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_manager = ConfigurationManager()
        config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n')
    except Exception as e:
        logger.exception(e)
        raise e