from fastapi import APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from fastapi import APIRouter, Header

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

from backend.app.services.context_compressor import (
    compress_context
)

from backend.app.services.user_service import (
    get_user
)


from backend.app.auth.jwt_handler import (
    get_current_user
)

from backend.app.services.audit_logger import (
    log_access
)

router = APIRouter()
security = HTTPBearer()

@router.post("/ask")
async def ask_question(
    query: str,
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    )
):
    
    token = credentials.credentials
   
    user = get_current_user(
    token
)
   
    results = hybrid_retrieve(
        query,department=user.role
    )


    if not has_sufficient_evidence(
        results
    ):

        log_access(
    user.username,
    user.role,
    query,
    "DENIED"
)

        return {

            "question": query,

            "answer":
            "I could not find this information in the provided documents."
        }

    compressed_results = compress_context(
    results
)

    context = build_context(
    compressed_results
)

    prompt = build_prompt(
        query,
        context
    )


    answer = generate_answer(
        prompt
    )

    if "I could not find this information" in answer:
        status = "NO_MATCH"
    else:
        status = "ANSWERED"

    
    log_access(
    user.username,
    user.role,
    query,
    status
)

    return {

        "question": query,

        "answer": answer
    }