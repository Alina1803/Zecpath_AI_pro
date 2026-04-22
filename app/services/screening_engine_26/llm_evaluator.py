import os
import json

try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    USE_LLM = True
except:
    USE_LLM = False


def evaluate_with_llm(question, answer, prompt_template):

    prompt = prompt_template + f"\n\nQuestion: {question}\nAnswer: {answer}"

    # ✅ If API available
    if USE_LLM and os.getenv("OPENAI_API_KEY"):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.choices[0].message.content

            return json.loads(content)

        except Exception as e:
            print(f"LLM failed, fallback used: {e}")

    # ✅ FALLBACK (NO API)
    return {
        "clarity": 7,
        "relevance": 7,
        "completeness": 6,
        "consistency": 7,
        "reason": "Fallback scoring (LLM unavailable)"
    }