from backend.app.services.hybrid_service import (
    hybrid_retrieve
)

results = hybrid_retrieve(
    "leave policy"
)

print(type(results))

print("\nRESULTS\n")

print(results)