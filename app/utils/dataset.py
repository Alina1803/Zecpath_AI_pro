import json
import os

def save_dataset(data, version="v1"):
    path = f"datasets/{version}/data.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)