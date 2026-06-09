from backend.app.services.document_ingestion import (
    load_all_pdfs
)

from backend.app.services.chunking import (
    chunk_documents
)

from backend.app.services.metadata import (
    enrich_chunk_metadata
)

documents = load_all_pdfs(
    "data/uploads"
)

chunks = chunk_documents(
    documents
)

chunks = enrich_chunk_metadata(
    chunks
)

print(chunks[0].metadata)