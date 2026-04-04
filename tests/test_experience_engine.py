import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.experience_parser import (
    extract_experience_entries,
    calculate_total_experience,
    detect_experience_gaps
)

from app.services.experience_relevance import compute_experience_relevance


resume_text = """
Software Engineer
Google
Jan 2020 - Mar 2023

Machine Learning Engineer
Amazon
Apr 2023 - Present
"""

job_description = """
Looking for Machine Learning Engineer with Python and AI experience
"""

experiences = extract_experience_entries(resume_text)

print("\nExtracted Experience:")
print(experiences)

total = calculate_total_experience(experiences)

print("\nTotal Experience:", total, "years")

gaps = detect_experience_gaps(experiences)

print("\nExperience Gaps:", gaps)

score = compute_experience_relevance(experiences, job_description)

print("\nExperience Relevance Score:", score)