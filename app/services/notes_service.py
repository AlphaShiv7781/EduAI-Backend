from app.services.retrieve_service import retrieve_chunks
from app.core.llm import generate_notes

def generate_study_notes(topic: str, top_k: int = 5):
    """
    Full RAG pipeline for generating study notes.
    """

    # 1️⃣ Retrieve relevant chunks from Qdrant
    retrieval_result = retrieve_chunks(topic, top_k)
    chunks = retrieval_result["results"]

    # 2️⃣ Combine chunks into a single context
    context = "\n\n".join(chunks)

    # 3️⃣ Generate notes using Gemini
    notes = generate_notes(context=context, topic=topic)

    return {
        "topic": topic,
        "notes": notes,
        "chunks_used": len(chunks)
    }
