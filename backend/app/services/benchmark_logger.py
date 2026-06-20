import csv
import os

CSV_FILE = "latency_metrics.csv"

def log_latency_metrics(
    request_latency,
    retrieval_latency,
    llm_latency,
    ttft
):

    file_exists = os.path.exists(
        CSV_FILE
    )

    with open(
        CSV_FILE,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(
            file
        )

        if not file_exists:

            writer.writerow([
                "request_latency",
                "retrieval_latency",
                "llm_latency",
                "ttft"
            ])

        writer.writerow([
            request_latency,
            retrieval_latency,
            llm_latency,
            ttft
        ])