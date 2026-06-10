from backend.app.services.document_ingestion import (
    load_all_pdfs
)

from backend.app.services.chunking import (
    chunk_documents
)

from backend.app.retrieval.bm25_retriever import (
    BM25Retriever
)

from backend.app.retrieval.hybrid_retriever import (
    HybridRetriever
)

from backend.app.services.retriever import (
    retrieve as vector_retrieve
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

hybrid = HybridRetriever(
    chunks
)

queries = [
    "vacation entitlement",
"remote working rules",
"health coverage",
"absence requirements",
"disciplinary actions"
]


bm25_score = 0
vector_score = 0
hybrid_score = 0


for query in queries:

    print("\n")
    print("=" * 60)

    print(
        f"QUERY: {query}"
    )

    print("=" * 60)

    # BM25
    bm25_result = bm25.retrieve(
        query,
        k=1
    )[0]

    print("\nBM25\n")

    print(
        bm25_result.page_content[:200]
    )

    bm25_score += int(
        input(
            "Relevant? (1/0): "
        )
    )

    # Vector
    vector_result = vector_retrieve(
        query,
        k=1
    )["documents"][0][0]

    print("\nVECTOR\n")

    print(
        vector_result[:200]
    )

    vector_score += int(
        input(
            "Relevant? (1/0): "
        )
    )

    # Hybrid
    hybrid_result = hybrid.retrieve(
        query,
        k=1
    )[0]

    print("\nHYBRID\n")

    print(
        hybrid_result[:200]
    )

    hybrid_score += int(
        input(
            "Relevant? (1/0): "
        )
    )


print("\n")
print("=" * 60)

print(
    f"BM25 Score: {bm25_score}"
)

print(
    f"Vector Score: {vector_score}"
)

print(
    f"Hybrid Score: {hybrid_score}"
)