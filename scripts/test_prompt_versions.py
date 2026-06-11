from backend.app.services.prompt_builder import (
    build_prompt
)

context = "Annual leave is 24 days."

query = "How many leave days do I get?"

print("\nV1\n")

print(
    build_prompt(
        query,
        context,
        version="v1"
    )
)

print("\nV2\n")

print(
    build_prompt(
        query,
        context,
        version="v2"
    )
)