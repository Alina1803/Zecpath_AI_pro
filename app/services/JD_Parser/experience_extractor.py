import re

def extract_experience(text):
    matches = re.findall(r'(\d+)\s+years', text)

    numbers = [int(m) for m in matches]

    return max(numbers) if numbers else 0