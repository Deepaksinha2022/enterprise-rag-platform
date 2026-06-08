from pathlib import Path


def list_uploaded_documents():

    upload_path = Path("data/uploads")

    documents = []

    for pdf_file in upload_path.glob("*.pdf"):

        documents.append(
            {
                "filename": pdf_file.name,
                "size_kb": round(
                    pdf_file.stat().st_size / 1024,
                    2
                )
            }
        )

    return documents