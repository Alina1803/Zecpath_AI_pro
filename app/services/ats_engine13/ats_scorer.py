from app.config.ca_domain_config import SKILL_DATABASE, SKILL_SYNONYMS

from app.services.ats_engine13.domain_detector import detect_ca_domain


def normalize(value):
    return str(value).lower().strip()


def normalize_list(data):

    if not isinstance(data, list):
        data = [data]

    clean = []

    for item in data:

        if isinstance(item, dict):

            item = item.get("skill") or item.get("name") or str(item)

        clean.append(normalize(item))

    return list(set(clean))


def expand_skills(skills):

    expanded = set()

    for skill in skills:

        skill = normalize(skill)

        expanded.add(skill)

        for main_skill, synonyms in SKILL_SYNONYMS.items():

            synonym_set = set(normalize(s) for s in synonyms)

            if skill == normalize(main_skill):

                expanded.update(synonym_set)

            if skill in synonym_set:

                expanded.add(normalize(main_skill))

    return list(expanded)


def safe_score(value):

    if isinstance(value, dict):

        if "total_experience_months" in value:

            return round(value["total_experience_months"] / 12, 1)

        return value.get("relevance_score", 0)

    return value or 0


def calculate_skill_score(resume_skills, jd_skills):

    resume_set = set(expand_skills(normalize_list(resume_skills)))

    jd_set = set(expand_skills(normalize_list(jd_skills)))

    domain_set = set(normalize(skill) for skill in SKILL_DATABASE)

    jd_score = (len(resume_set & jd_set) / len(jd_set) * 100) if jd_set else 0

    domain_score = (
        (len(resume_set & domain_set) / len(domain_set) * 100) if domain_set else 0
    )

    return round((jd_score * 0.7) + (domain_score * 0.3), 2)


def calculate_experience_score(resume_exp, jd_exp):

    if jd_exp == 0:
        return 70

    if resume_exp >= jd_exp:
        return 100

    return round((resume_exp / jd_exp) * 100, 2)


def calculate_education_score(resume_edu, jd_edu):

    if not jd_edu:
        return 70

    resume_set = set(normalize_list(resume_edu))

    jd_set = set(normalize_list(jd_edu))

    return 100 if (resume_set & jd_set) else 40


def calculate_score(resume_data, jd_data, semantic_raw=0):

    skill_score = calculate_skill_score(
        resume_data.get("skills", []), jd_data.get("skills", [])
    )

    exp_score = calculate_experience_score(
        safe_score(resume_data.get("experience", 0)),
        safe_score(jd_data.get("experience", 0)),
    )

    edu_score = calculate_education_score(
        resume_data.get("education", []), jd_data.get("education", [])
    )

    semantic_score = round(safe_score(semantic_raw) * 100, 2)

    final_score = round(
        skill_score * 0.30
        + exp_score * 0.25
        + edu_score * 0.20
        + semantic_score * 0.25,
        2,
    )

    breakdown = {
        "skills_score": skill_score,
        "experience_score": exp_score,
        "education_score": edu_score,
        "semantic_score": semantic_score,
        "matched_skills": list(
            set(normalize_list(resume_data.get("skills", [])))
            & set(normalize_list(jd_data.get("skills", [])))
        ),
        "missing_skills": list(
            set(normalize_list(jd_data.get("skills", [])))
            - set(normalize_list(resume_data.get("skills", [])))
        ),
    }

    domain_analysis = detect_ca_domain(resume_data)

    if domain_analysis["domain_match"]:

        final_score += 5

    return {
        "final_score": min(round(final_score, 2), 100),
        "breakdown": breakdown,
        "domain_analysis": domain_analysis,
        "recommendation": (
            "Suitable for CA Domain"
            if domain_analysis["domain_match"]
            else "Not Suitable for CA Domain"
        ),
    }
