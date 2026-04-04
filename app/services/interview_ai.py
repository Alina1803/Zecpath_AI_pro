import openai
import json

openai.api_key = "YOUR_API_KEY"


def evaluate_interview(transcript: str) -> dict:
    prompt = f"""
    Evaluate this interview response:

    Transcript:
    {transcript}

    Score (0-10) on:
    - communication
    - technical
    - confidence

    Return JSON only.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["choices"][0]["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {"error": "Invalid JSON from model"}