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
    generate_answer,
    generate_answer_stream
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

from backend.app.services.cache_service import (
    redis_client
)

from backend.app.services.cache_service import (
    get_cached_answer,
    save_cached_answer
)

from backend.app.services.cache_service import (
    cache_stats
)

from backend.app.services.cache_service import (
    search_semantic_cache,
    store_semantic_cache,
    semantic_cache_saves_count,
    search_semantic_cache_async,
    store_semantic_cache_async
)

from backend.app.services.cache_service import (
    semantic_cache_stats
)

from fastapi.responses import StreamingResponse
import asyncio

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

    cache_key = f"query:{query.lower()}"

    cached_answer = get_cached_answer(
    query
)
    if not cached_answer:

        semantic_answer = await search_semantic_cache_async(
            query
        )

        if semantic_answer:

            print(
                "[SEMANTIC CACHE HIT]"
            )

            return {
                "question": query,
                "answer": semantic_answer
            }

    print(
    f"Cache Hit Ratio: {cache_stats():.2f}%"
)
    
    print(
    f"Semantic Cache Hits: {semantic_cache_stats()}"
)

    print(
    f"LLM Calls Saved: {semantic_cache_saves_count()}"
)
    if cached_answer:

        return {
        "question": query,
        "answer": cached_answer
    }
    
    results = await hybrid_retrieve(
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

    answer = await generate_answer(
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

    save_cached_answer(
    query,
    answer
)
    
    await store_semantic_cache_async(
    query,
    answer
)
    
    return {

        "question": query,

        "answer": answer
    }

@router.post("/ask-stream")
async def ask_stream(
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

    import time

    retrieval_start = start_timer()

    cache_key = f"query:{query.lower()}"

    cached_answer = get_cached_answer(
    query
)
    if not cached_answer:

        semantic_answer = await search_semantic_cache_async(
            query
        )

        if semantic_answer:

            print(
                "[SEMANTIC CACHE HIT]"
            )

            return {
                "question": query,
                "answer": semantic_answer
            }

    print(
    f"Cache Hit Ratio: {cache_stats():.2f}%"
)
    
    print(
    f"Semantic Cache Hits: {semantic_cache_stats()}"
)

    print(
    f"LLM Calls Saved: {semantic_cache_saves_count()}"
)
    if cached_answer:

        return {
        "question": query,
        "answer": cached_answer
    }
    
    results = await hybrid_retrieve(
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

    answer_stream = generate_answer_stream(
        prompt
    )

#     output_tokens = estimate_tokens(
#     answer_stream
# )
    
#     estimated_cost = estimate_cost(
#     input_tokens,
#     output_tokens
# )

#     log_metric(
#     "estimated_cost_usd",
#     estimated_cost
# )

    llm_duration = end_timer(
    llm_start
)

    log_metric(
    "llm_latency",
    llm_duration
)

    # if "I could not find this information" in answer_stream:
    #     status = "NO_MATCH"
    # else:
    #     status = "ANSWERED"

    
#     log_access(
#     user.username,
#     user.role,
#     query,
#     status
# )
    request_duration = end_timer(
    request_start
)
    log_metric(
    "request_latency",
    request_duration
)

#     save_cached_answer(
#     query,
#     answer_stream
# )
    
#     await store_semantic_cache_async(
#     query,
#     answer_stream
# )
    
    import json

    async def generate():

        first_token_sent = False

        async for chunk in answer_stream:

            try:

                data = json.loads(
                    chunk
                )

                token = data.get(
                    "response",
                    ""
                )

                if token:

                    if not first_token_sent:

                        first_token_time = (
                            time.time() -
                            request_start
                        )

                        print(
                            f"[METRIC] ttft: {first_token_time:.3f}s"
                        )

                        first_token_sent = True

                    yield (
                        f"data: {token}\n\n"
                    )

            except Exception:

                continue

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )

@router.get("/stream-test")
async def stream_test():

  
    async def generate():

        for word in [
            "Hello",
            "from",
            "Enterprise",
            "RAG"
        ]:

            yield word + " "

            await asyncio.sleep(1)

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )

@router.get("/stream-answer")
async def stream_answer():

    print("ROUTE HIT")

    answer = (
        "This is a streaming response "
        "from the Enterprise RAG Platform."
    )

    async def generate():

        print("STREAM STARTED")

        for word in answer.split():

            print(word)

            yield f"data: {word}\n\n"

            await asyncio.sleep(0.2)

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )