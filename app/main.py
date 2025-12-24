from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.ingest import router as ingest_router
from app.api.retrieve import router as retrieve_router
from app.api.notes import router as notes_router
from app.api.qa import router as qa_router

load_dotenv()

app = FastAPI(title="EduAI Backend")

app.include_router(ingest_router, prefix="/ingest", tags=["Ingest"])
app.include_router(retrieve_router, prefix="/retrieve", tags=["Retrieve"])
app.include_router(notes_router, prefix="/notes", tags=["Notes"])
app.include_router(qa_router, prefix="/qa", tags=["Q&A"])

@app.get("/")
def root():
    return {"message": "EduAI backend running"}
