from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.ingest import router as ingest_router

load_dotenv()

app = FastAPI(title="EduAI Backend")

app.include_router(ingest_router, prefix="/ingest")

@app.get("/")
def root():
    return {"message": "EduAI backend running"}
