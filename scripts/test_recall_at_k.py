from data.benchmark_queries import (
    benchmark_queries
)

from backend.app.services.retriever import (
    retrieve
)

k = 3

correct = 0

total = len(
    benchmark_queries
)

for item in benchmark_queries:

    query = item["query"]

    expected = item["expected"]

    results = retrieve(
        query,
        k=k
    )

    retrieved_docs = (
        results["documents"][0]
    )

    found = False

    for doc in retrieved_docs:

        if expected.lower() in doc.lower():

            found = True

            break

    if found:

        correct += 1

        print(
            f"✅ {query}"
        )

    else:

        print(
            f"❌ {query}"
        )

accuracy = (
    correct / total
) * 100

print("\n")

print(
    f"Recall@{k}: {accuracy:.2f}%"
)