from src.data_science_project import logger
from src.data_science_project.pipeline.data_ingestion_pipeline import (
    DataIngestionTrainingPipeline,
)
from src.data_science_project.pipeline.data_validation_piptline import (
    DataValidationTrainingPipeline,
)
from src.data_science_project.pipeline.data_transformation_pipeline import (
    DataTransformationTrainingPipeline,
)
from src.data_science_project.pipeline.model_trainer_pipeline import (
    ModelTrainerTrainingPipeline,
)
from src.data_science_project.pipeline.model_evaluate import (
    ModelEvaluateTrainingPipeline,
)


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.initiate_model_trainer()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluate stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    model_evaluate = ModelEvaluateTrainingPipeline()
    model_evaluate.initiate_model_evaluation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e
