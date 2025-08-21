import sys, os
import numpy as np
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()  # looks for a .env file in the current and parent directories
print(".env loaded (if present)")
def get_key(name, default):
    return os.getenv(name, default)
PROJECT_ROOT = Path.cwd().parent
DATA_DIR = PROJECT_ROOT / "data"
print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)