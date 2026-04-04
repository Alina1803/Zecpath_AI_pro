import json
from faker import Faker

fake = Faker()

def generate_resume():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "skills": ["Python", "ML", "NLP"],
        "experience": fake.job()
    }

def save_sample_data(n=5):
    data = [generate_resume() for _ in range(n)]
    
    with open("data/processed/sample_resumes.json", "w") as f:
        json.dump(data, f, indent=4)