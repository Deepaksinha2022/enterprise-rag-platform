from fastapi import APIRouter

from backend.app.services.retriever import (
    retrieve
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

    results = retrieve(
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

    return {
        "question": query,
        "answer": answer
    }