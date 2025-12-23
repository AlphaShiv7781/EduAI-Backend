from fastapi import APIRouter, UploadFile, File
from app.services.ingest_service import ingest_pdf

router = APIRouter()

@router.post("/pdf")
def ingest_pdf_api(file: UploadFile = File(...)):
    return ingest_pdf(file)