from backend.app.services.document_ingestion import (
    load_all_pdfs
)

from backend.app.services.chunking import (
    chunk_documents
)

from backend.app.retrieval.hybrid_retriever import (
    HybridRetriever
)

documents = load_all_pdfs(
    "data/uploads"
)

chunks = chunk_documents(
    documents
)

hybrid = HybridRetriever(
    chunks
)


def hybrid_retrieve(
    query,
    k=3,
    department=None
):

    return hybrid.retrieve(
        query,
        k,
        department
    )