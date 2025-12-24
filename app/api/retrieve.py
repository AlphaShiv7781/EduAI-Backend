from fastapi import APIRouter
from app.services.retrieve_service import retrieve_chunks

router = APIRouter()


@router.get("/")
def retrieve(query: str, top_k: int = 5):

    """
    Retrieve relevant chunks for a user query.
    """
    return retrieve_chunks(query, top_k)