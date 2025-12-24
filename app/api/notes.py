from fastapi import APIRouter
from app.services.notes_service import generate_study_notes

router = APIRouter()

@router.get("/")
def generate_notes_api(topic: str, top_k: int = 5):
    """
    API endpoint to generate study notes using RAG.
    """
    return generate_study_notes(topic, top_k)
