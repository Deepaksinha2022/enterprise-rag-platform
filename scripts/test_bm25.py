from backend.app.services.document_ingestion import (
    load_all_pdfs
)

from backend.app.services.chunking import (
    chunk_documents
)

from backend.app.retrieval.bm25_retriever import (
    BM25Retriever
)


documents = load_all_pdfs(
    "data/uploads"
)

chunks = chunk_documents(
    documents
)

retriever = BM25Retriever(
    chunks
)

results = retriever.retrieve(
    "leave policy"
)

print(
    results[0].page_content[:500]
)