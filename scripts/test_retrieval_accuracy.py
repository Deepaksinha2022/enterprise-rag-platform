from data.benchmark_queries import (
    benchmark_queries
)

from backend.app.services.retriever import (
    retrieve
)


total = len(
    benchmark_queries
)

correct = 0


for item in benchmark_queries:

    query = item["query"]

    expected = item["expected"]

    results = retrieve(
        query,
        k=1
    )

    retrieved_text = (
        results["documents"][0][0]
    )

    if expected.lower() in retrieved_text.lower():

        correct += 1

        print(
            f"✅ {query}"
        )

    else:

        print(
            f"❌ {query}"
        )

        print(
            f"Expected: {expected}"
        )

        print(
            f"Retrieved: {retrieved_text[:100]}"
        )


accuracy = (
    correct / total
) * 100


print("\n")

print(
    f"Correct: {correct}"
)

print(
    f"Total: {total}"
)

print(
    f"Accuracy: {accuracy:.2f}%"
)