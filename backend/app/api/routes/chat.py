from fastapi import APIRouter

from backend.app.services.hybrid_service import (
    hybrid_retrieve
)

from backend.app.services.prompt_builder import (
    build_context,
    build_prompt
)

from backend.app.services.evidence_checker import (
    has_sufficient_evidence
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

    if not has_sufficient_evidence(
        results
    ):

        return {

            "question": query,

            "answer":
            "I could not find this information in the provided documents."
        }

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