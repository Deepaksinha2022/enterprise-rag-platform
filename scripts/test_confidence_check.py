from backend.app.services.evidence_checker import (
    has_sufficient_evidence
)

print(

    has_sufficient_evidence(
        []
    )
)

print(

    has_sufficient_evidence(
        [
            "chunk1"
        ]
    )
)

print(

    has_sufficient_evidence(
        [
            "chunk1",
            "chunk2"
        ],
        min_chunks=2
    )
)