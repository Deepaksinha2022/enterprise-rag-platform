import redis

from sentence_transformers import util

from backend.app.services.embeddings import (
    generate_embeddings, generate_embeddings_async
)

semantic_cache = {}

semantic_cache_hits = 0

semantic_cache_saves = 0

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True

)

def get_cached_answer(
    query
):

    cache_key = (
        f"query:{query.lower()}"
    )

    result = redis_client.get(
        cache_key
    )

    if result:

        cache_hit()

    else:

        cache_miss()

    return result

def save_cached_answer(
    query,
    answer,
    ttl=3600
):
    cache_key = f"query:{query.lower()}"

    redis_client.setex(
        cache_key,
        ttl,
        answer
    )

def cache_hit():

    global cache_hits

    cache_hits += 1

    print(
        "[CACHE HIT]"
    )

cache_hits = 0
cache_misses = 0

def cache_miss():

    global cache_misses

    cache_misses += 1

    print(
        "[CACHE MISS]"
    )

def cache_stats():

    total = (
        cache_hits +
        cache_misses
    )

    if total == 0:
        return 0

    return (
        cache_hits /
        total
    ) * 100

def store_semantic_cache(
    query,
    answer
):

    embedding = generate_embeddings(
        [query]
    )[0]

    semantic_cache[query] = {

        "embedding": embedding,

        "answer": answer
    }

async def store_semantic_cache_async(
    query,
    answer
):

    embedding = (
        await generate_embeddings_async(
            [query]
        )
    )[0]

    semantic_cache[query] = {

        "embedding": embedding,

        "answer": answer
    }

def search_semantic_cache(
    query,
    threshold=0.80
):

    query_embedding = generate_embeddings(
        [query]
    )[0]

    for cached_query, data in semantic_cache.items():

        similarity = util.cos_sim(
            query_embedding,
            data["embedding"]
        ).item()
       
        print(
    f"Similarity: {similarity:.3f}"
)

        if similarity >= threshold:

            global semantic_cache_hits

            global semantic_cache_saves

            semantic_cache_hits += 1

            semantic_cache_saves += 1

            return data["answer"]

    return None

async def search_semantic_cache_async(
    query,
    threshold=0.80
):

    query_embedding = (
        await generate_embeddings_async(
            [query]
        )
    )[0]

    for cached_query, data in semantic_cache.items():

        similarity = util.cos_sim(
            query_embedding,
            data["embedding"]
        ).item()

        print(
            f"Similarity: {similarity:.3f}"
        )

        if similarity >= threshold:

            global semantic_cache_hits
            global semantic_cache_saves

            semantic_cache_hits += 1
            semantic_cache_saves += 1

            return data["answer"]

    return None

def semantic_cache_stats():

    return semantic_cache_hits

def semantic_cache_saves_count():

    return semantic_cache_saves