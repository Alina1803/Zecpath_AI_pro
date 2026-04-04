import os


def ensure_directories():
    directories = [
        "data/raw",
        "data/processed",
        "data/datasets",
        "logs"
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)