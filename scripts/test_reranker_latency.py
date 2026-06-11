import time

from backend.app.retrieval.reranker import (
    rerank
)

docs = [

    "Annual Leave Policy",

    "Sick Leave Policy",

    "Attendance Policy",

    "Employee Benefits",

    "Introduction"
]

start = time.time()

results = rerank(
    "sick leave policy",
    docs
)

end = time.time()

print(
    f"Reranker Latency: {end - start:.4f}s"
)