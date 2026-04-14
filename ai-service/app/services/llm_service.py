import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(user_input: str, retrieved_context: str):
    prompt = f"""
You are a smart assistant helping users avoid unnecessary expenses or being misled.

User situation:
{user_input}

Relevant knowledge:
{retrieved_context}

Return your response STRICTLY in JSON format like this:

{{
  "suggestions": ["question1", "question2"],
  "risk_level": "low | medium | high"
}}

Rules:
- Suggestions must be short and actionable questions
- Do not accuse anyone
- Be polite
- risk_level should reflect seriousness of situation
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {
            "suggestions": ["Unable to parse response, please rephrase input"],
            "risk_level": "unknown"
        }