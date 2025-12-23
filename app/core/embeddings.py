#IF WE USED GEMINI THE WE MUST HAVE THIS FILE
# from dotenv import load_dotenv
# load_dotenv() 

# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/embedding-001"
# )

#USING LOCAL EMBEDDINGS INSTEAD
from sentence_transformers import SentenceTransformer

# Load model once (this happens at server start)
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_documents(texts: list[str]) -> list[list[float]]:
    """
    Convert list of text chunks into vectors using a local model.
    """
    return model.encode(texts, show_progress_bar=False).tolist()

