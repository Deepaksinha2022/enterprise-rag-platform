from backend.app.services.document_ingestion import (
    load_all_pdfs
)

from backend.app.services.chunking import (
    chunk_documents
)

from backend.app.retrieval.bm25_retriever import (
    BM25Retriever
)

from backend.app.services.retriever import (
    retrieve
)


documents = load_all_pdfs(
    "data/uploads"
)

chunks = chunk_documents(
    documents
)

bm25 = BM25Retriever(
    chunks
)

queries = [

    "leave policy",

    "vacation rules",

    "employee benefits"
]


for query in queries:

    print("\n")
    print("=" * 60)

    print(
        f"QUERY: {query}"
    )

    print("=" * 60)

    bm25_results = bm25.retrieve(
        query,
        k=1
    )

    print("\nBM25:\n")

    print(
        bm25_results[0]
        .page_content[:300]
    )

    vector_results = retrieve(
        query,
        k=1
    )

    print("\nVECTOR:\n")

    print(
        vector_results
        ["documents"][0][0][:300]
    )