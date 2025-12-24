import os
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Study notes generation
def generate_notes(context: str, topic: str) -> str:
    """
    Generate structured study notes using Gemini (google-genai).
    """

    prompt = f"""
You are a study assistant.

Using ONLY the information provided below, generate clear and structured study notes.

Topic:
{topic}

Context:
{context}

Instructions:
- Use headings and bullet points
- Keep explanations simple and exam-oriented
- Do not add external information
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


#Q&A with memory
def generate_answer_with_memory(context: str, question: str, history: list) -> str:
    """
    Answer a question using retrieved context and chat history.
    """

    history_text = ""
    for msg in history:
        history_text += f"{msg['role'].upper()}: {msg['content']}\n"

    prompt = f"""
You are a conversational AI assistant.

Conversation so far:
{history_text}

Use ONLY the information in the context below to answer.

Context:
{context}

User question:
{question}

If the answer is not present in the context, say:
"I could not find this information in the provided documents."
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
