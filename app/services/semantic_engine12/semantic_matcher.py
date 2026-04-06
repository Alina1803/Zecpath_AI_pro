from .embedder import get_embedding
from .similarity_engine import compute_similarity

def semantic_match(resume_text, job_description):
    resume_vec = get_embedding(resume_text)
    jd_vec = get_embedding(job_description)

    similarity = compute_similarity(resume_vec, jd_vec)

    return {
        "semantic_similarity": similarity
    }

def match_skills(resume_skills, jd_skills):
    return compute_similarity(
        get_embedding(", ".join(resume_skills)),
        get_embedding(", ".join(jd_skills))
    )

def match_experience(resume_exp, jd_desc):
    return compute_similarity(
        get_embedding(resume_exp),
        get_embedding(jd_desc)
    )

def match_projects(projects, jd_desc):
    if not projects:
        return 0.0

    scores = []
    jd_vec = get_embedding(jd_desc)

    for proj in projects:
        proj_vec = get_embedding(proj)
        scores.append(compute_similarity(proj_vec, jd_vec))

    return max(scores) if scores else 0.0