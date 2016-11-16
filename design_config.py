import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Database Setup
DESIGN_DB_URL = 'mysql://root:Kony@123@localhost/design'
APPS_DB_URL = 'mysql://root:Kony@123@localhost/archaeaappsdb'

MOCK_NERD_RESPONSE = False