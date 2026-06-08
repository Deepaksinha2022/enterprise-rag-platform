from pathlib import Path
from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile
from backend.app.services.pdf_loader import load_pdf

router = APIRouter()

UPLOAD_DIR = "data/uploads"

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    Path(UPLOAD_DIR).mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    documents = load_pdf(file_path)

    return {
        "filename": file.filename,
        "pages_loaded": len(documents),
        "status": "uploaded"
    }