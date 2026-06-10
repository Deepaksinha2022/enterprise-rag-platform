from pathlib import Path
from backend.app.services.pdf_loader import load_pdf

def load_all_pdfs(folder_path: str):

    all_documents = []

    pdf_files = Path(folder_path).glob("*.pdf")

    for pdf_file in pdf_files:

        documents = load_pdf(str(pdf_file))

        filename = pdf_file.name

        if "HR" in filename:
            department = "HR"

        elif "Finance" in filename:
            department = "Finance"

        elif "Engineering" in filename:
            department = "Engineering"

        else:
            department = "General"


        if department == "Finance":
            access_level = "manager"
        else:
            access_level = "employee"


        for doc in documents:

            doc.metadata["filename"] = filename

            doc.metadata["department"] = department

            doc.metadata["access_level"] = access_level

        all_documents.extend(documents)

    return all_documents