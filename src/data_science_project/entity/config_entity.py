from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    """
    Configuration for data ingestion.
    """

    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    status_file: str
    all_schema: dict


@dataclass
class DataTransformationConfig:
    """
    Data Transformation configuration class.
    """

    root_dir: Path
    data_path: Path
