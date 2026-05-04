import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "role_weights41.json")

def load_weights():
    with open(FILE_PATH, "r") as f:
        return json.load(f)