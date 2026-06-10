def build_context(results):

    return "\n\n".join(results)

def build_prompt(
    query,
    context
):

    prompt = f"""
You are a helpful assistant.

Use only the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt