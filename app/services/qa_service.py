from app.services.retrieve_service import retrieve_chunks
from app.core.llm import generate_answer_with_memory
from app.core.memory import get_history, add_message


def answer_question(question: str, session_id: str, top_k: int = 5):
    history = get_history(session_id)

    retrieval_result = retrieve_chunks(question, top_k)
    chunks = retrieval_result["results"]

    # 🚨 NEW: Handle empty retrieval gracefully
    if not chunks:
        friendly_response = (
            f"I couldn’t find information related to **'{question}'** "
            "in the documents you’ve uploaded so far.\n\n"
            "👉 Try uploading relevant study material, and I’ll be happy to help!"
        )

        add_message(session_id, "user", question)
        add_message(session_id, "assistant", friendly_response)

        return {
            "session_id": session_id,
            "question": question,
            "answer": friendly_response,
            "chunks_used": 0
        }

    # Normal RAG flow
    context = "\n\n".join(chunks)

    answer = generate_answer_with_memory(
        context=context,
        question=question,
        history=history
    )

    add_message(session_id, "user", question)
    add_message(session_id, "assistant", answer)

    return {
        "session_id": session_id,
        "question": question,
        "answer": answer,
        "chunks_used": len(chunks)
    }
