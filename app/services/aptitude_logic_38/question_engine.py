import json

def load_questions():
    with open("app.services.aptitude_logic_38.data.aptitude_questions38.json") as f:
        return json.load(f)

def get_questions(category="logical_reasoning"):
    data = load_questions()
    return data.get(category, [])