import joblib

def load_model(path: str):
    try:
        model = joblib.load(path)
        return model
    except Exception as e:
        raise RuntimeError(f"Error loading model: {e}")