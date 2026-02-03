import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_clause(clause):
    prompt = f"""
Explain this contract clause in simple business English for an Indian SME owner.
Explain:
1. What it means
2. Why it is risky
3. Suggest a safer alternative clause

Clause:
{clause}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
