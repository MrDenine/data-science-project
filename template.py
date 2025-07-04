import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

proect_name = "data_science_project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{proect_name}/__init__.py",
    f"src/{proect_name}/components/__init__.py",
    f"src/{proect_name}/utils/__init__.py",
    f"src/{proect_name}/utils/common.py",
    f"src/{proect_name}/config/__init__.py",
    f"src/{proect_name}/config/configuration.yaml",
    f"src/{proect_name}/pipeline/__init__.py",
    f"src/{proect_name}/entity/__init__.py",
    f"src/{proect_name}/entity/config_entity.py",
    f"src/{proect_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating file: {file_path}")

    else:
        logging.info(
            f"File already exists: {file_path} and is not empty, skipping creation."
        )
