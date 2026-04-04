import re

def extract_experience(text):
    return re.findall(r'(\d+\+?\s*years)', text)