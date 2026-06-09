from backend.app.services.document_ingestion import (
    load_all_pdfs
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


documents = load_all_pdfs(
    "data/uploads"
)

sizes = [500, 1000, 1500]

for size in sizes:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=size,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        documents
    )

    print("=" * 50)

    print(f"Chunk Size: {size}")

    print(f"Chunks Created: {len(chunks)}")

    print("=" * 50)
    print(len(chunks[0].page_content))
    print(chunks[0])
    print(type(chunks[0]))