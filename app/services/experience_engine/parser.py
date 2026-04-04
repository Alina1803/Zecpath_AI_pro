import re
import spacy
import dateparser

nlp = spacy.load("en_core_web_sm")


def extract_dates(text):

    pattern = r'([A-Za-z]{3,9}\s?\d{4}|Present)'
    matches = re.findall(pattern, text)

    dates = []

    for m in matches:
        if m.lower() == "present":
            dates.append("Present")
        else:
            d = dateparser.parse(m)
            if d:
                dates.append(d.strftime("%b %Y"))

    return dates


def parse_experience(resume_text):

    roles = []

    lines = resume_text.split("\n")

    for i, line in enumerate(lines):

        doc = nlp(line)

        company = None

        for ent in doc.ents:
            if ent.label_ == "ORG":
                company = ent.text

        dates = extract_dates(line)

        if company and dates:

            role = {
                "title": lines[i-1] if i > 0 else "",
                "company": company,
                "start": dates[0],
                "end": dates[1] if len(dates) > 1 else "Present"
            }

            roles.append(role)

    return roles