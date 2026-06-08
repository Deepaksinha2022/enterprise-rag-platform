from pathlib import Path
from backend.app.services.pdf_loader import load_pdf

def load_all_pdfs(folder_path: str):

    all_documents = []

    pdf_files = Path(folder_path).glob("*.pdf")

    for pdf_file in pdf_files:

        documents = load_pdf(str(pdf_file))

        for doc in documents:

            doc.metadata["filename"] = pdf_file.name

        all_documents.extend(documents)

    return all_documents