from backend.app.services.hybrid_service import (
    hybrid_retrieve
)

query = "sick leave policy"

results = hybrid_retrieve(
    query,
    k=5
)

print("\nHYBRID RESULTS\n")

for i, doc in enumerate(
    results,
    start=1
):

    print(
        f"{i}. {doc[:100]}"
    )

    print("-" * 40)