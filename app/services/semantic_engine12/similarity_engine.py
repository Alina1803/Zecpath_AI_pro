from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def get_embedding(text: str):
    return model.encode(text)   # ✅ FIXED


def compute_similarity(vec1, vec2):
    return float(
        cosine_similarity(
            vec1.reshape(1, -1),
            vec2.reshape(1, -1)
        )[0][0]
    )


def semantic_similarity(resume_text: str, job_description: str) -> float:
    if not resume_text or not job_description:
        return 0.0

    emb1 = get_embedding(resume_text)
    emb2 = get_embedding(job_description)

    return round(compute_similarity(emb1, emb2), 3)