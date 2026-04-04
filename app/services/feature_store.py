def extract_features(parsed_data: dict) -> dict:
    return {
        "skill_count": len(parsed_data.get("skills", [])),
        "experience": parsed_data.get("experience", 0)
    }