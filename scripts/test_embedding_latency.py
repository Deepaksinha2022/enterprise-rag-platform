import time

from backend.app.services.embeddings import (
    generate_embeddings
)

start = time.time()

embedding = generate_embeddings(
    ["sick leave policy"]
)

end = time.time()

print(
    f"Embedding Latency: {end - start:.4f}s"
)