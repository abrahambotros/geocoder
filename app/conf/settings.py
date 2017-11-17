"""
Settings configuration file.
"""

# External imports
import os
from dotenv import find_dotenv, load_dotenv

# Internal imports
# - N/A


# Load .env file.
load_dotenv(find_dotenv())

# Constants from .env.
GMAPS_API_KEY = os.environ.get("GMAPS_API_KEY", "")
HERE_APP_ID = os.environ.get("HERE_APP_ID", "")
HERE_APP_CODE = os.environ.get("HERE_APP_CODE", "")
