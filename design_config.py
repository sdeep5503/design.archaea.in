import os
import json


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
with open(PROJECT_ROOT + '/design.config.json') as config_file:
    config = json.load(config_file)


# Config variables
DESIGN_DB_URL = config['DATABASE_URL']
MOCK_NERD_RESPONSE = config['MOCK_NERD_RESPONSE']
EXTERNAL_REQUEST_TIMEOUT = config['EXTERNAL_REQUEST_TIMEOUT']