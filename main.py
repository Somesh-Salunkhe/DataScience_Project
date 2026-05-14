from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainingPipeline
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

STAGE_NAME = "Data Validation"

try:
        logger.info(f">>>>> {STAGE_NAME} started <<<<<")
        obj = DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation"


try:
        logger.info(f">>>>> {STAGE_NAME} started <<<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Training"

try:
        logger.info(f">>>>> {STAGE_NAME} started <<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
except Exception as e:
        logger.exception(e)
        raise e