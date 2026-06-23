from app.services.experience_engine.experience_parser import (
    extract_experience,
    detect_gaps,
    detect_overlaps,
)


class ExperienceEngine:

    @staticmethod
    def analyze(text):

        result = extract_experience(text)

        experiences = result["experiences"]

        total_months = result["total_experience_months"]

        gaps = detect_gaps(experiences)

        overlaps = detect_overlaps(experiences)

        years = round(total_months / 12, 1)

        if years <= 2:
            level = "junior"

        elif years <= 5:
            level = "mid"

        else:
            level = "senior"

        return {
            "years": years,
            "level": level,
            "gaps": gaps,
            "overlaps": overlaps,
            "experiences": experiences,
        }
