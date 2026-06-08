from backend.app.services.document_ingestion import (
    load_all_pdfs
)

documents = load_all_pdfs(
    "data/uploads"
)
print(
    f"Total Pages Loaded: {len(documents)}"
)
print("\n")
print(
    documents[0].metadata
)