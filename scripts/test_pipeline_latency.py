import time

from backend.app.services.document_ingestion import (
    load_all_pdfs
)

from backend.app.services.chunking import (
    chunk_documents
)

start = time.time()

documents = load_all_pdfs(
    "data/uploads"
)

print(
    f"Load PDFs: {time.time() - start:.2f}s"
)

start = time.time()

chunks = chunk_documents(
    documents
)

print(
    f"Chunking: {time.time() - start:.2f}s"
)