from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(answer, expected_answer):
    emb1 = model.encode([answer])
    emb2 = model.encode([expected_answer])

    score = cosine_similarity(emb1, emb2)[0][0]

    return round(score * 10, 2)  # scale to 10