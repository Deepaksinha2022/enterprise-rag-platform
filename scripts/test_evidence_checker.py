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
            "Annual Leave Policy"
        ]
    )
)