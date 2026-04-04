from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')     

def get_embedding(text, model):
    if not isinstance(text, str):
        print("Invalid input: not string")
        return []

    if not text.strip():
        print("Empty text")
        return []

    try:
        return model.encode(text).tolist()
    except Exception as e:
        print(f"Embedding error: {e}")
        return []