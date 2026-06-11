import time

from backend.app.services.hybrid_service import (
    hybrid_retrieve
)


query = "sick leave policy"

start_time = time.time()

results = hybrid_retrieve(
    query,
    k=5
)

end_time = time.time()

latency = end_time - start_time

print("\nLATENCY TEST\n")

print(
    f"Latency: {latency:.4f} seconds"
)