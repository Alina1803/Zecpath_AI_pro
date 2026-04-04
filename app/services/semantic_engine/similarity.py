from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(vec1, vec2):
    if vec1 is None or vec2 is None:
        return 0.0
    return cosine_similarity([vec1], [vec2])[0][0]