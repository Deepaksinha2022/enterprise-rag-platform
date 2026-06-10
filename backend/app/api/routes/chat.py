from fastapi import APIRouter

from backend.app.services.hybrid_service import (
    hybrid_retrieve
)
from backend.app.services.prompt_builder import (
    build_context,
    build_prompt
)

from backend.app.services.llm import (
    generate_answer
)


router = APIRouter()


@router.post("/ask")
async def ask_question(
    query: str
):

    results = hybrid_retrieve(
        query
    )

    context = build_context(
        results
    )

    prompt = build_prompt(
        query,
        context
    )

    answer = generate_answer(
        prompt
    )

    # sources = []

    # for metadata in results["metadatas"][0]:

    #     sources.append(

    #     f"{metadata['filename']} | "

    #     f"Page {metadata['page'] + 1}"
    # )
    return {

    "question": query,

    "answer": answer
    # , "sources": sources
}

results = hybrid_retrieve(
    "leave policy"
)

print(type(results))
print(results)