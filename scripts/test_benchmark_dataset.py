from data.benchmark_queries import (
    benchmark_queries
)

print(
    f"Queries: {len(benchmark_queries)}"
)

for item in benchmark_queries:

    print(
        item["query"]
    )