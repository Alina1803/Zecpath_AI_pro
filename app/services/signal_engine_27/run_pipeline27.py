import os
import json
from datetime import datetime

from app.services.signal_engine_27.signal_engine import SignalEngine


BASE_DIR = os.getcwd()

INPUT_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "output_26"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "output_27"
)


def load_latest_output():
    files = sorted(os.listdir(INPUT_PATH))
    latest = files[-1]

    with open(os.path.join(INPUT_PATH, latest), encoding="utf-8") as f:
        return json.load(f)


def save_output(data):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    file_path = os.path.join(
        OUTPUT_DIR,
        f"signal_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return file_path


def run():
    print("Running Signal Analysis...")

    data = load_latest_output()
    engine = SignalEngine()

    results = []

    for item in data["results"]:
        signal = engine.evaluate(item["answer"])

        item.update(signal)
        results.append(item)

    final_output = {
        "meta": data["meta"],
        "results": results
    }

    path = save_output(final_output)

    print("Signal analysis completed")
    print(f"Saved at: {path}")


if __name__ == "__main__":
    run()