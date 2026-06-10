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

retriever = HybridRetriever(
    chunks
)

results = retriever.retrieve(
    "leave policy"
)

for idx, chunk in enumerate(results):

    print("\n")

    print(
        f"RESULT {idx+1}"
    )

    print("=" * 50)

    print(
        chunk[:300]
    )