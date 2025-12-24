from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.ingest import router as ingest_router
from app.api.retrieve import router as retrieve_router

load_dotenv()

app = FastAPI(title="EduAI Backend")

app.include_router(ingest_router, prefix="/ingest", tags=["Ingest"])
app.include_router(retrieve_router, prefix="/retrieve", tags=["Retrieve"])

@app.get("/")
def root():
    return {"message": "EduAI backend running"}
