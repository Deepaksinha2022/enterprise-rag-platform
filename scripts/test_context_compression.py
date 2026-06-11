from backend.app.services.context_compressor import (
    compress_context
)

chunks = [

    "A" * 500,

    "B" * 500
]

compressed = compress_context(
    chunks
)

for chunk in compressed:

    print(
        len(chunk)
    )