import os, sys, yaml
from .logger import logger

# Contain all Class to load config and messages

config_file = "config.yml"
messages_file = "messages.yml"

class Config(object):
    def __init__(self):
        # No need to check if file is present as it is already check by logger
        with open(config_file) as file:
            config = yaml.safe_load(file)
            for k in config:
                if isinstance(config[k], dict):
                    setattr(self, k, type('dict_data', (), config[k]))
                else:
                    setattr(self, k, config[k])