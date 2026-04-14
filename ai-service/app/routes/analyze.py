from fastapi import APIRouter
from app.services.analyze_service import analyze_text

router = APIRouter()

@router.post("/analyze")
def analyze(data: dict):
    text = data.get("text")
    user_id = data.get("user_id", "default_user")

    result = analyze_text(text, user_id)

    return result