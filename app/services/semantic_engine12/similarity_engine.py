from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ✅ Load model ONCE (very important)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def get_embedding(text: str):
    return model.encode([text])[0]


def semantic_similarity(resume_text: str, job_description: str) -> float:
    """
    Returns similarity score between 0 and 1
    """

    emb1 = get_embedding(resume_text)
    emb2 = get_embedding(job_description)

    score = cosine_similarity([emb1], [emb2])[0][0]

    return round(float(score), 3)