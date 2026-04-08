import json

# Load knowledge base once
with open("app/rag/knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)


def analyze_text(text: str):
    text_lower = text.lower()

    matched_suggestions = []

    for item in knowledge_base:
        for keyword in item["keywords"]:
            if keyword in text_lower:
                matched_suggestions.extend(item["suggestions"])
                break

    if not matched_suggestions:
        matched_suggestions.append("No strong suggestions found. Ask for more clarification.")

    return {
        "suggestions": matched_suggestions
    }