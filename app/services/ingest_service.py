import tempfile
from pypdf import PdfReader
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

from app.core.embeddings import embed_documents
from app.utils.splitter import split_text

# Connect to Qdrant (Docker)
qdrant = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "edu_docs"


def ingest_pdf(file):
    """
    Complete ingestion pipeline using LOCAL embeddings.
    """

    # 1️⃣ Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file.file.read())
        pdf_path = tmp.name

    # 2️⃣ Read PDF text
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""

    # 3️⃣ Split into chunks
    chunks = split_text(full_text)

    # 4️⃣ Generate local embeddings
    vectors = embed_documents(chunks)

    # 5️⃣ Create Qdrant collection (only once, safe to call)
    qdrant.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=len(vectors[0]),
            distance=Distance.COSINE
        )
    )

    # 6️⃣ Store vectors + text
    qdrant.upload_collection(
        collection_name=COLLECTION_NAME,
        vectors=vectors,
        payload=[{"text": chunk} for chunk in chunks]
    )

    return {
        "status": "success",
        "chunks_stored": len(chunks),
        "embedding_type": "local"
    }
