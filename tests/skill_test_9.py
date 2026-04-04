import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from app.services.skill_extractor import extract_skills

resume_text = """
Python developer with experience in FastAPI, Docker, AWS, and SQL.
Worked with Machine Learning using Scikit-learn and Pandas.
"""

skills = extract_skills(resume_text)

print("Extracted Skills:")
print(skills)