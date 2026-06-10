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
    k=3,
    department="General"
)

print("\nFILTERED RESULTS\n")
print(results)
for doc in results["documents"][0]:

    print("-" * 50)

    print(
        doc[:300]
    )