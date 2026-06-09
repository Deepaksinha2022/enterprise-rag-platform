
from backend.app.services.document_ingestion import (
    load_all_pdfs
)

from backend.app.services.chunking import (
    chunk_documents
)

from backend.app.services.embeddings import (
    generate_embeddings
)

documents = load_all_pdfs(
    "data/uploads"
)

chunks = chunk_documents(
    documents
)

texts = [
    chunk.page_content
    for chunk in chunks[:5]
]

embeddings = generate_embeddings(
    texts
)

print(
    f"Chunks: {len(texts)}"
)

print(
    f"Embeddings: {len(embeddings)}"
)
print("embedding_type",type(embeddings))
print(
    f"Embedding Dimension: {len(embeddings[0])}"
)