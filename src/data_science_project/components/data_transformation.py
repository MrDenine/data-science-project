import os
from src.data_science_project.entity.config_entity import DataTransformationConfig
from src.data_science_project import logger
from sklearn.model_selection import train_test_split
import pandas as pd


class DataTransformation:
    """
    Data Transformation class to handle data preprocessing.
    """

    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info(f"Train and test data saved at {self.config.root_dir}")
        logger.info(f"Train data shape: {train.shape}, Test data shape: {test.shape}")

        print(f"Train data shape: {train.shape}, Test data shape: {test.shape}")
