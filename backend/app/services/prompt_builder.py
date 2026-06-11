from backend.app.prompts.prompt_registry import (
    PROMPTS
)

def build_context(results):

    return "\n\n".join(results)

def build_prompt(
    query,
    context,
    version="v2"
):
    system_prompt = PROMPTS[
    version
]   
    return f"""
{system_prompt}

Context:
{context}

Question:
{query}

Answer:
"""

