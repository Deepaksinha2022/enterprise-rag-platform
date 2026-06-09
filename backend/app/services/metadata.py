def enrich_chunk_metadata(chunks):

    for idx, chunk in enumerate(chunks):

        chunk.metadata["chunk_id"] = idx

    return chunks