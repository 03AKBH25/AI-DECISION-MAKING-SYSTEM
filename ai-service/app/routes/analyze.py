from fastapi import APIRouter
from app.services.analyze_service import analyze_text

router = APIRouter()

@router.post("/analyze")
def analyze(data: dict):
    text = data.get("text")

    result = analyze_text(text)

    return {
        "input": text,
        "result": result
    }