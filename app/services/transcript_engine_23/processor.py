from .normalizer import normalize_text
from .finance_extractor import extract_ca_skills

def process_transcript(transcript):
    full_text = ""
    all_topics = []

    for segment in transcript["segments"]:
        clean_text = normalize_text(segment["text"])
        segment["text"] = clean_text

        skills = extract_ca_skills(clean_text)
        segment["finance_skill_tags"] = skills
        all_topics.extend(skills)

        full_text += clean_text + " "

    transcript["full_text"] = full_text.strip()
    transcript["detected_topics"] = list(set(all_topics))

    return transcript