from backend.app.jobs.ingestion_job import (
    run_ingestion_job
)

count = run_ingestion_job()

print(
    "Chunks Processed:",
    count
)