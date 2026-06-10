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


test_queries = [

    "leave policy",

    "vacation rules",

    "employee benefits",

    "attendance policy",

    "work from home"
]


bm25_score = 0

vector_score = 0


for query in test_queries:

    print("\n")
    print("=" * 60)

    print(query)

    bm25_result = bm25.retrieve(
        query,
        k=1
    )[0]

    vector_result = retrieve(
        query,
        k=1
    )["documents"][0][0]

    print("\nBM25:")
    print(bm25_result.page_content[:200])

    bm25_relevant = int(
        input(
            "\nRelevant? (1/0): "
        )
    )

    bm25_score += bm25_relevant

    print("\nVECTOR:")
    print(vector_result[:200])

    vector_relevant = int(
        input(
            "\nRelevant? (1/0): "
        )
    )

    vector_score += vector_relevant


print("\n")
print("=" * 60)

print(
    "BM25 Score:",
    bm25_score
)

print(
    "Vector Score:",
    vector_score
)