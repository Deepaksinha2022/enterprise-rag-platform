from backend.app.retrieval.bm25_retriever import (
    BM25Retriever
)

from backend.app.services.retriever import (
    retrieve as vector_retrieve
)


class HybridRetriever:

    def __init__(self, chunks):

        self.chunks = chunks

        self.bm25 = BM25Retriever(
            chunks
        )

    def weighted_fusion(
        self,
        bm25_results,
        vector_results
    ):

        scores = {}

        bm25_weight = 0.3
        vector_weight = 0.7

        # BM25 contribution
        for rank, chunk in enumerate(
            bm25_results,
            start=1
        ):

            text = chunk.page_content

            scores[text] = (
                scores.get(text, 0)
                + bm25_weight * (
                    1 / (60 + rank)
                )
            )

        # Vector contribution
        for rank, text in enumerate(
            vector_results["documents"][0],
            start=1
        ):

            scores[text] = (
                scores.get(text, 0)
                + vector_weight * (
                    1 / (60 + rank)
                )
            )

        ranked_results = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            text
            for text, score
            in ranked_results
        ]

    def retrieve(
        self,
        query,
        k=3
    ):

        bm25_results = self.bm25.retrieve(
            query,
            k
        )

        vector_results = vector_retrieve(
            query,
            k
        )

        fused_results = self.weighted_fusion(
            bm25_results,
            vector_results
        )

        return fused_results[:k]