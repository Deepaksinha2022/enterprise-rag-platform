from backend.app.retrieval.query_rewriter import (
    rewrite_query
)

from backend.app.retrieval.query_expander import (
    expand_query
)


def process_query(
    query
):

    rewritten_query = rewrite_query(
        query
    )

    expanded_queries = expand_query(
        rewritten_query
    )

    return expanded_queries