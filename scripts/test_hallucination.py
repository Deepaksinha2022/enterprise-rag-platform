from backend.app.services.prompt_builder import (
    build_prompt
)

context = """
Employees receive 24 days
of annual leave annually.
"""

query = """
What is the maternity leave policy?
"""

prompt = build_prompt(
    query,
    context,
    version="v2"
)

print(prompt)