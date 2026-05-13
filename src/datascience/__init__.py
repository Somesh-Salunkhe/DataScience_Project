'''
Custom Logging Functionality
'''

# Imports
import os
import sys
import logging

# Logging structure
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

'''
%(asctime)s : Time
%(levelname)s : Level name (info, warning)
%(module)s : Module name 
%(message)s : Message 
'''

# Logging directory
log_dir = 'logs'
log_filepath = os.path.join(log_dir, "logging.log")

# Make directory
os.makedirs(log_dir, exist_ok=True)

# Basic config
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Initialize logger
logger = logging.getLogger('datascience_logger')