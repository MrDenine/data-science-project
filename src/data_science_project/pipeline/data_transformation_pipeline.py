from src.data_science_project.config.configuration import ConfigurationManager
from src.data_science_project.components.data_transformation import DataTransformation
from src.data_science_project import logger
from pathlib import Path

STAGE_NAME = "Data Transformation stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as file:
                status = file.read().split(" ")[-1].strip()
                if status == "True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(
                        config=data_transformation_config
                    )
                    data_transformation.train_test_splitting()
                else:
                    logger.info("Data Validation failed. Skipping Data Transformation.")
                    raise Exception(
                        "Data Validation failed. Skipping Data Transformation."
                    )
        except Exception as e:
            logger.exception(f"Error during data transformation: {e}")
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
