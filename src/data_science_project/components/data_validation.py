import pandas as pd
from src.data_science_project.entity.config_entity import DataValidationConfig
from src.data_science_project import logger


class DataValidation:
    """
    Class to validate data.
    """

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validate if all columns in the data match the schema.
        """
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation status: {validation_status}\n")
                else:
                    validation_status = True
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation status: {validation_status}\n")
            return validation_status

        except Exception as e:
            logger.exception(f"Exception occurred during data validation: {e}")
            raise e
