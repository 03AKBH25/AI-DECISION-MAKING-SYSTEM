from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze")
def analyze(data: dict):
    return {
        "message": "Analyze endpoint working",
        "input": data
    }