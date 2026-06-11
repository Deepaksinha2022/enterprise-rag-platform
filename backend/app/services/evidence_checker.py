def has_sufficient_evidence(
    results,
    min_chunks=1
):

    if not results:

        return False

    if len(results) < min_chunks:

        return False

    return True