from backend.app.services.observability import (
    estimate_cost
)

cost = estimate_cost(
    500,
    200
)

print(
    "Estimated Cost:",
    cost
)