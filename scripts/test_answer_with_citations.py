from backend.app.services.embeddings import (
    generate_embeddings
)

from backend.app.services.vector_store import (
    search_chunks
)


query = "sick leave policy"

query_embedding = generate_embeddings(
    [query]
)[0]

results = search_chunks(
    query_embedding,
    k=3
)

documents = results["documents"][0]

metadatas = results["metadatas"][0]

answer = documents[0][:300]

print("\nANSWER\n")

print(answer)

print("\nSOURCES\n")

for index, metadata in enumerate(
    metadatas,
    start=1
):

    print(
        f"[{index}] "
        f"{metadata['filename']} | "
        f"Page {metadata['page'] + 1}"
    )
