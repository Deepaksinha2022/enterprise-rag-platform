from backend.app.services.user_service import (
    get_user
)

from backend.app.services.retriever import (
    retrieve
)

user = get_user(
    "finance_user"
)

results = retrieve(
    "policy",
    department="Finance"
)

print(
    results["metadatas"][0][0]["department"]
)