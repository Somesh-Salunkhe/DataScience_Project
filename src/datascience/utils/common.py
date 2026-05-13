# Imports
import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


# Reading YAML file
@ensure_annotations
def read_yaml(yaml_path : Path) -> ConfigBox:
    """
    Reads YAML file and returns contents

    Args:
        yaml_path (str) : file path 

    Raises:
        ValueError : if YAML file is empty
        e: Empty error

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(yaml_path) as file:
            content = yaml.safe_load(file)
            logger.info(f"YAML file {yaml_path} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty.")
    except Exception as e:
        raise e
    

# Create directories
@ensure_annotations
def create_directory(paths: list, verbose = True):
    """
    Create list of directories

    Args:
        paths = list of path of directories
        ignore_log(bool, optional) ignore if multiple directories are to be created.
     """
    
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


# Saving files in JSON
@ensure_annotations
def save_json(path:Path, data: dict):
    """
    Save JSON data

    Args:
        path (Path): Path to JSON file
        data (Dict): data to be saved in JSON file
    """

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")


# Load JSON
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load JSON file

    Args:
        path (Path): Path to JSON file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """

    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


# Save Model
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """

    joblib.dump(value=data , filename=path)
    logger.info(f"Binary file saved at : {path}")

# Load Model
@ensure_annotations
def load_bin(path:Path)-> Any:
    """
    Load binary data

    Args:
        path (Path): path to binary file
    
    Returns:
        Any: Object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data