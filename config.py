import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.resolve()
CORE_DIR = os.path.join(BASE_DIR, 'core')
INPUT_CSV_PATH = os.path.join(BASE_DIR, 'data', 'input_csv')
OUTPUT_CSV_PATH = os.path.join(BASE_DIR, 'data', 'output_csv')
META_PATH = os.path.join(BASE_DIR, 'data', 'meta')
