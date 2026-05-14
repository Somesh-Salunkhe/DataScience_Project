from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.datascience import logger


STAGE_NAME = "Data Ingestion"

try:
        logger.info(f">>>>> {STAGE_NAME} started <<<<<")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e