from backend.app.services.embeddings import (
    generate_embeddings
)

from backend.app.services.vector_store import (
    search_chunks
)

query = "leave policy"

query_embedding = generate_embeddings(
    [query]
)[0]

results = search_chunks(
    query_embedding,
    k=3
)

for doc, meta in zip(
    results["documents"][0],
    results["metadatas"][0]
):

    print("\nDOCUMENT\n")

    print(doc[:200])

    print("\nSOURCE\n")

    print(
        f"{meta['filename']} | Page {meta['page'] + 1}"
    )

    print("-" * 50)