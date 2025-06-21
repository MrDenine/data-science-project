import os
import urllib.request as request
from src.data_science_project.entity.config_entity import DataIngestionConfig
from src.data_science_project import logger
import zipfile


## component for data ingestion
class DataIngestion:
    """
    Data ingestion component to handle data downloading and extraction.
    """

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        """
        Download data from the source URL.
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url, filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file: {filename} with headers:\n {headers}")

        else:
            logger.info(
                f"File already exists: {self.config.local_data_file}. Skipping download."
            )

    def extract_data(self):
        """
        Extract downloaded data.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted data to: {unzip_path}")
