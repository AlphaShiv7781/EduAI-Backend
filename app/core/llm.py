import os
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

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
