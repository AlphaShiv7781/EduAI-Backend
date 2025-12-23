import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

load_dotenv()

QDRANT_HOST = os.getenv("QDRANT_HOST")
QDRANT_PORT = int(os.getenv("QDRANT_PORT"))

qdrant = QdrantClient(
    host=QDRANT_HOST,
    port=QDRANT_PORT,
)

def create_collection():
    """
    Recreates (clears + creates) the edu_documents collection.
    """
    qdrant.recreate_collection(
        collection_name="edu_documents",
        vectors_config=VectorParams(
            size=768,              # Gemini embedding size
            distance=Distance.COSINE  
        )
    )
