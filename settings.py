from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

# Load the local environment from the .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# If there are system level
GENERATE_ICONS_PATH = environ.get("GENERATE_ICONS_PATH")
GENERATE_PACKS_PATH = environ.get("GENERATE_PACKS_PATH")
GENERATE_URL = environ.get("GENERATE_URL")
