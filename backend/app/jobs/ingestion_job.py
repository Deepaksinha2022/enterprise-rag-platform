from backend.app.services.document_ingestion import (
    load_all_pdfs
)

from backend.app.services.chunking import (
    chunk_documents
)

from backend.app.services.metadata import (
    enrich_chunk_metadata
)

from backend.app.services.embeddings import (
    generate_embeddings
)

from backend.app.services.vector_store import (
    store_chunks
)


def run_ingestion_job():

    documents = load_all_pdfs(
        "data/uploads"
    )

    chunks = chunk_documents(
        documents
    )

    chunks = enrich_chunk_metadata(
        chunks
    )

    texts = [
        chunk.page_content
        for chunk in chunks
    ]

    embeddings = generate_embeddings(
        texts
    )

    store_chunks(
        chunks,
        embeddings
    )

    return len(chunks)