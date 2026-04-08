import json
import os


def load_test_candidates(input_folder):
    candidates = []

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json"):
            path = os.path.join(input_folder, file_name)

            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                candidates.append(data)

    return candidates