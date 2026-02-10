#IF WE USED GEMINI THE WE MUST HAVE THIS FILE
# from dotenv import load_dotenv
# load_dotenv() 

# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/embedding-001"
# )

#USING LOCAL EMBEDDINGS INSTEAD
# from sentence_transformers import SentenceTransformer

# # Load model once (this happens at server start)
# model = SentenceTransformer("all-MiniLM-L6-v2")

# def embed_documents(texts: list[str]) -> list[list[float]]:
#     """
#     Convert list of text chunks into vectors using a local model.
#     """
#     return model.encode(texts, show_progress_bar=False).tolist()


#USING JINA EMBEDDINGS INSTEAD
import os
import requests
from typing import List

JINA_API_KEY = os.getenv("JINA_API_KEY")

JINA_URL = "https://api.jina.ai/v1/embeddings"

HEADERS = {
    "Authorization": f"Bearer {JINA_API_KEY}",
    "Content-Type": "application/json"
}

def embed_documents(texts: List[str]) -> List[List[float]]:
    response = requests.post(
        JINA_URL,
        headers=HEADERS,
        json={
            "model": "jina-embeddings-v2-base-en",
            "input": texts
        },
        timeout=60
    )

    response.raise_for_status()
    data = response.json()

    return [item['embedding'] for item in data['data']]
