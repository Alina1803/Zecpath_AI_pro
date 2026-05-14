import re
from datetime import datetime
from typing import List, Dict, Any


CURRENT_YEAR = datetime.now().year


class AdvancedExperienceParser:
    """
    Enterprise-Level ATS Experience Parser

    Features:
    -----------------------------------
    ✓ Experience extraction
    ✓ Company extraction
    ✓ Role extraction
    ✓ Date normalization
    ✓ Overlap handling
    ✓ Career gap analysis
    ✓ Seniority detection
    ✓ Stability scoring
    ✓ Experience scoring
    ✓ Resume timeline generation
    ✓ ATS-ready structured output
    """

    def __init__(self):

        self.date_patterns = [

            # 2019 - 2022
            r'(?P<start>\d{4})\s*[-–to]+\s*(?P<end>\d{4}|present|Present)',

            # Jan 2020 - Feb 2023
            r'(?P<start_month>[A-Za-z]{3,9})\s*(?P<start_year>\d{4})\s*[-–to]+\s*(?P<end_month>[A-Za-z]{3,9}|present|Present)\s*(?P<end_year>\d{4}|present|Present)?'
        ]

        self.role_keywords = [
            "engineer",
            "developer",
            "manager",
            "analyst",
            "consultant",
            "architect",
            "lead",
            "intern",
            "specialist",
            "scientist",
            "designer"
        ]

    # ---------------------------------------------------
    # EXTRACT EXPERIENCE BLOCKS
    # ---------------------------------------------------

    def extract_experience_blocks(
        self,
        text: str
    ) -> List[Dict]:

        lines = text.split("\n")

        experiences = []

        for i, line in enumerate(lines):

            for pattern in self.date_patterns:

                match = re.search(
                    pattern,
                    line,
                    re.IGNORECASE
                )

                if match:

                    start_year = (
                        int(match.group("start"))
                        if match.groupdict().get("start")
                        else int(match.group("start_year"))
                    )

                    end_value = (
                        match.group("end")
                        if match.groupdict().get("end")
                        else match.group("end_year")
                    )

                    if (
                        not end_value or
                        str(end_value).lower() == "present"
                    ):
                        end_year = CURRENT_YEAR
                    else:
                        end_year = int(end_value)

                    role = self.extract_role(
                        lines,
                        i
                    )

                    company = self.extract_company(
                        lines,
                        i
                    )

                    experiences.append({

                        "start_year": start_year,

                        "end_year": end_year,

                        "duration": max(
                            end_year - start_year,
                            0
                        ),

                        "role": role,

                        "company": company
                    })

        return experiences

    # ---------------------------------------------------
    # ROLE EXTRACTION
    # ---------------------------------------------------

    def extract_role(
        self,
        lines,
        index
    ) -> str:

        search_range = max(0, index - 2)

        for i in range(search_range, index + 1):

            line = lines[i].strip().lower()

            for keyword in self.role_keywords:

                if keyword in line:
                    return lines[i].strip()

        return "Unknown Role"

    # ---------------------------------------------------
    # COMPANY EXTRACTION
    # ---------------------------------------------------

    def extract_company(
        self,
        lines,
        index
    ) -> str:

        if index == 0:
            return "Unknown Company"

        previous_line = lines[index - 1].strip()

        if len(previous_line) > 2:
            return previous_line

        return "Unknown Company"

    # ---------------------------------------------------
    # REMOVE DUPLICATES
    # ---------------------------------------------------

    def remove_duplicate_experience(
        self,
        experiences
    ):

        unique = []

        seen = set()

        for exp in experiences:

            key = (
                exp["start_year"],
                exp["end_year"],
                exp["role"]
            )

            if key not in seen:

                seen.add(key)

                unique.append(exp)

        return unique

    # ---------------------------------------------------
    # MERGE OVERLAPS
    # ---------------------------------------------------

    def merge_overlapping_experience(
        self,
        experiences
    ):

        if not experiences:
            return []

        experiences = sorted(
            experiences,
            key=lambda x: x["start_year"]
        )

        merged = [experiences[0]]

        for current in experiences[1:]:

            previous = merged[-1]

            if (
                current["start_year"] <=
                previous["end_year"]
            ):

                previous["end_year"] = max(
                    previous["end_year"],
                    current["end_year"]
                )

            else:
                merged.append(current)

        return merged

    # ---------------------------------------------------
    # TOTAL EXPERIENCE
    # ---------------------------------------------------

    def calculate_total_experience(
        self,
        experiences
    ) -> int:

        total = 0

        for exp in experiences:

            total += (
                exp["end_year"] -
                exp["start_year"]
            )

        return total

    # ---------------------------------------------------
    # GAP ANALYSIS
    # ---------------------------------------------------

    def analyze_career_gaps(
        self,
        experiences
    ):

        gaps = []

        if len(experiences) <= 1:
            return gaps

        experiences = sorted(
            experiences,
            key=lambda x: x["start_year"]
        )

        for i in range(1, len(experiences)):

            previous = experiences[i - 1]
            current = experiences[i]

            gap = (
                current["start_year"] -
                previous["end_year"]
            )

            if gap > 1:

                gaps.append({

                    "gap_years": gap,

                    "between": (
                        previous["end_year"],
                        current["start_year"]
                    )
                })

        return gaps

    # ---------------------------------------------------
    # EXPERIENCE LEVEL
    # ---------------------------------------------------

    def classify_experience_level(
        self,
        years
    ) -> str:

        if years == 0:
            return "Fresher"

        elif years <= 2:
            return "Junior"

        elif years <= 5:
            return "Mid-Level"

        elif years <= 10:
            return "Senior"

        elif years <= 15:
            return "Lead"

        return "Architect / Expert"

    # ---------------------------------------------------
    # EXPERIENCE SCORE
    # ---------------------------------------------------

    def calculate_experience_score(
        self,
        years
    ) -> int:

        return min(years * 10, 100)

    # ---------------------------------------------------
    # STABILITY SCORE
    # ---------------------------------------------------

    def calculate_stability_score(
        self,
        gaps
    ) -> int:

        if len(gaps) == 0:
            return 100

        if len(gaps) == 1:
            return 80

        if len(gaps) == 2:
            return 60

        return 40

    # ---------------------------------------------------
    # MAIN PARSER
    # ---------------------------------------------------

    def parse(
        self,
        resume_text: str
    ) -> Dict[str, Any]:

        raw_experience = self.extract_experience_blocks(
            resume_text
        )

        unique_experience = (
            self.remove_duplicate_experience(
                raw_experience
            )
        )

        processed_experience = (
            self.merge_overlapping_experience(
                unique_experience
            )
        )

        total_experience = (
            self.calculate_total_experience(
                processed_experience
            )
        )

        career_gaps = (
            self.analyze_career_gaps(
                processed_experience
            )
        )

        experience_level = (
            self.classify_experience_level(
                total_experience
            )
        )

        experience_score = (
            self.calculate_experience_score(
                total_experience
            )
        )

        stability_score = (
            self.calculate_stability_score(
                career_gaps
            )
        )

        return {

            "total_experience_years":
            total_experience,

            "experience_level":
            experience_level,

            "experience_score":
            experience_score,

            "stability_score":
            stability_score,

            "career_gaps":
            career_gaps,

            "experience_timeline":
            processed_experience,

            "positions_detected":
            len(processed_experience),

            "analysis": {

                "candidate_seniority":
                experience_level,

                "career_stability":
                "High"
                if stability_score >= 80
                else "Moderate",

                "gap_count":
                len(career_gaps),

                "ats_recommendation":
                "Recommended"
                if experience_score >= 60
                else "Needs Review"
            }
        }


# ---------------------------------------------------
# TESTING
# ---------------------------------------------------

if __name__ == "__main__":

    sample_resume = """

    ABC Technologies
    Software Engineer
    2018 - 2020

    XYZ Systems
    Senior Backend Developer
    2020 - Present

    """

    parser = AdvancedExperienceParser()

    result = parser.parse(sample_resume)

    from pprint import pprint

    pprint(result)