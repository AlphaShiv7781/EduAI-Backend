from app.core.qdrant_connection import qdrant
from app.core.embeddings import embed_documents

COLLECTION_NAME = "edu_docs"


def retrieve_chunks(query: str, top_k: int = 5):
    # 1️⃣ Embed the user query
    query_vector = embed_documents([query])[0]

    # 2️⃣ Query Qdrant (MODERN API)
    response = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        prefetch=[],                 # no hybrid search for now
        query=query_vector,
        limit=top_k,
        with_payload=True
    )

    # 3️⃣ Extract text from payload
    results = [point.payload["text"] for point in response.points]

    return {
        "query": query,
        "top_k": top_k,
        "results": results
    }
