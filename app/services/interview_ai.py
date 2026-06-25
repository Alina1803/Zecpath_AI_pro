import os
import json
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def evaluate_interview(transcript: str) -> dict:

    prompt = f"""
Evaluate this interview response:

Transcript:
{transcript}

Score (0-10):
- communication
- technical
- confidence

Return JSON only.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    content = response["choices"][0]["message"]["content"]

    try:
        return json.loads(content)

    except Exception:

        return {"error": "Invalid JSON from model"}
