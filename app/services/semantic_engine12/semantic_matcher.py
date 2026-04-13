from .embedder import get_embedding
from .similarity_engine import compute_similarity


# -----------------------------
# SAFE EMBEDDING WRAPPER
# -----------------------------
def safe_embed(text):
    if not text or str(text).strip() == "":
        return None
    return get_embedding(str(text))


# -----------------------------
# FULL TEXT SEMANTIC MATCH
# -----------------------------
def semantic_match(resume_text, job_description):

    vec1 = safe_embed(resume_text)
    vec2 = safe_embed(job_description)

    if vec1 is None or vec2 is None:
        return {"semantic_similarity": 0.0}

    return {
        "semantic_similarity": round(compute_similarity(vec1, vec2), 3)
    }


# -----------------------------
# SKILL MATCH
# -----------------------------
def match_skills(resume_skills, jd_skills):

    # Flatten skills if categorized
    if isinstance(resume_skills, dict):
        resume_skills = sum(resume_skills.values(), [])

    if isinstance(jd_skills, dict):
        jd_skills = sum(jd_skills.values(), [])

    if not jd_skills:
        return 0.0   # ✅ correct

    if not resume_skills:
        return 0.0   # ✅ important fix

    matched = set(resume_skills) & set(jd_skills)

    return len(matched) / len(jd_skills)


# -----------------------------
# EXPERIENCE MATCH
# -----------------------------
def match_experience(resume_exp, jd_exp):

    if not resume_exp or not jd_exp:
        return 0.0

    text1 = f"{resume_exp} years experience"
    text2 = f"{jd_exp} years experience"

    vec1 = safe_embed(text1)
    vec2 = safe_embed(text2)

    if vec1 is None or vec2 is None:
        return 0.0

    return round(compute_similarity(vec1, vec2), 3)


# -----------------------------
# EDUCATION MATCH
# -----------------------------
def match_education(resume_edu, jd_education):

    if not resume_edu or not jd_education:
        return 0.0

    # ✅ FIX: convert list → string
    if isinstance(resume_edu, list):
        resume_edu = " ".join(resume_edu)

    if isinstance(jd_education, list):
        jd_education = " ".join(jd_education)

    return compute_similarity(
        get_embedding(resume_edu),
        get_embedding(jd_education)
    )

# -----------------------------
# PROJECT MATCH
# -----------------------------
def match_projects(projects, jd_desc):

    if not projects or not jd_desc:
        return 0.0

    jd_vec = safe_embed(jd_desc)

    if jd_vec is None:
        return 0.0

    scores = []

    for proj in projects:
        proj_vec = safe_embed(proj)

        if proj_vec is None:
            continue

        score = compute_similarity(proj_vec, jd_vec)
        scores.append(score)

    return round(max(scores), 3) if scores else 0.0