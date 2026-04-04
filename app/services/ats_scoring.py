from typing import Dict, List


def calculate_skill_match(resume_skills: List[str], job_skills: List[str]) -> float:
    if not job_skills:
        return 0.0

    matched = set(resume_skills).intersection(set(job_skills))
    return len(matched) / len(job_skills)


def calculate_experience_score(candidate_exp: int, required_exp: int) -> float:
    if required_exp == 0:
        return 1.0
    return min(candidate_exp / required_exp, 1.0)


def calculate_ats_score(parsed_resume: Dict, job_requirements: Dict) -> Dict:
    resume_skills = parsed_resume.get("skills", [])
    resume_exp = parsed_resume.get("experience_years", 0)

    job_skills = job_requirements.get("required_skills", [])
    required_exp = job_requirements.get("min_experience_years", 0)

    skill_score = calculate_skill_match(resume_skills, job_skills)
    experience_score = calculate_experience_score(resume_exp, required_exp)

    # Weighted scoring
    final_score = (0.7 * skill_score) + (0.3 * experience_score)

    return {
        "skill_match_score": round(skill_score * 100, 2),
        "experience_score": round(experience_score * 100, 2),
        "final_ats_score": round(final_score * 100, 2)
    }