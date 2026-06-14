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

from backend.app.services.observability import (
    start_timer,
    end_timer,
    log_metric,
    estimate_tokens
)
from backend.app.services.observability import (
    start_timer,
    end_timer,
    log_metric,
    estimate_tokens,
    estimate_cost
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
    request_start = start_timer()

    retrieval_start = start_timer()
    
    results = hybrid_retrieve(
        query,department=user.role
    )

    retrieval_duration = end_timer(
    retrieval_start
)
    log_metric(
    "retrieval_latency",
    retrieval_duration
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
    
    estimated_tokens = estimate_tokens(
    context
)
    input_tokens = estimated_tokens

    log_metric(
    "estimated_context_tokens",
    estimated_tokens
)

    context_length = len(
    context
)

    log_metric(
    "context_characters",
    context_length
)

    prompt = build_prompt(
        query,
        context
    )

    llm_start = start_timer()

    answer = generate_answer(
        prompt
    )

    output_tokens = estimate_tokens(
    answer
)
    
    estimated_cost = estimate_cost(
    input_tokens,
    output_tokens
)

    log_metric(
    "estimated_cost_usd",
    estimated_cost
)


    llm_duration = end_timer(
    llm_start
)

    log_metric(
    "llm_latency",
    llm_duration
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
    request_duration = end_timer(
    request_start
)
    log_metric(
    "request_latency",
    request_duration
)

    return {

        "question": query,

        "answer": answer
    }