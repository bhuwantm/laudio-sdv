import os
import pathlib
from dotenv import load_dotenv

BASE_DIR = pathlib.Path(__file__).parent.resolve()
CORE_DIR = os.path.join(BASE_DIR, 'core')
INPUT_CSV_PATH = os.path.join(BASE_DIR, 'data', 'input_csv')
OUTPUT_CSV_PATH = os.path.join(BASE_DIR, 'data', 'output_csv')
META_PATH = os.path.join(BASE_DIR, 'data', 'meta')


load_dotenv()

DB_DRIVER = os.getenv('DB_DRIVER')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
