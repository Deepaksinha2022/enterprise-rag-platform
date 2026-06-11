from backend.app.services.prompt_builder import (
    build_prompt
)

context = "Annual leave entitlement is 24 days."

query = "How many leave days do I get?"

for version in [

    "v1",

    "v2"

]:

    print("\n")

    print(
        "=" * 50
    )

    print(
        f"PROMPT VERSION: {version}"
    )

    print(
        "=" * 50
    )

    print(

        build_prompt(
            query,
            context,
            version=version
        )
    )