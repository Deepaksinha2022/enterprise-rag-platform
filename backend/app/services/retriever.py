from backend.app.services.embeddings import (
    generate_embeddings
)

from backend.app.services.vector_store import (
    search_chunks
)


def retrieve(
    query,
    k=3
):

    query_embedding = generate_embeddings(
        [query]
    )[0]

    results = search_chunks(
        query_embedding,
        k
    )

    return results