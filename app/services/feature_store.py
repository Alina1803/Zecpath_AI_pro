def extract_features(parsed_data: dict) -> dict:

    features = {
        "skill_count": len(parsed_data.get("skills", [])),
        "experience": int(parsed_data.get("experience_years", 0)),
    }

    print("\n===== FEATURE STORE =====")
    print("PARSED DATA:", parsed_data)
    print("FEATURES:", features)

    return features
