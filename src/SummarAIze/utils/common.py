import os
from box.exceptions import BoxValueError
from box import ConfigBox
from pathlib import Path
from typing import Any
import yaml
from ensure import ensure_annotations
from SummarAIze.logging import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads the YAML file and returns
    
    Args:
        path_to_yaml (str): Path to the YAML file

    Raises:
        ValueError: If yaml file is empty
        e: If yaml file is not valid
        
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        logger.exception(
            f"yaml file: {path_to_yaml} has yaml syntax errors")
        raise
    except Exception as e:
        logger.exception(
            f"yaml file: {path_to_yaml} could not be loaded")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories
    
    Args:
        path_to_directories (list): List of path of directories
        ignore (bool, optional): Ignore if dir exists. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
            
            
@ensure_annotations
def get_size(path: Path) -> str:
    """Get size in KB
    
    Args:
        path (str): Path of the file
    
    Returns:
        str: Size of the file in KB 
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"