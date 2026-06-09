def build_context(results):

    documents = results["documents"][0]

    context = "\n\n".join(
        documents
    )

    return context

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