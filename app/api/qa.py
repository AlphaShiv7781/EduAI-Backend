from fastapi import APIRouter
from app.services.qa_service import answer_question

router = APIRouter()


@router.get("/")
def qa(
    question: str,
    session_id: str,
    top_k: int = 5
):
    """
    Conversational RAG Q&A endpoint.
    """
    return answer_question(question, session_id, top_k)
