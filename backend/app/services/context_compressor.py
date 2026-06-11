def compress_context(
    results,
    max_chars=200
):

    compressed = []

    for chunk in results:

        compressed.append(
            chunk[:max_chars]
        )

    return compressed