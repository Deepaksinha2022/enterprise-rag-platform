import pandas as pd

df = pd.read_csv(
    "latency_metrics.csv"
)

for col in [
    "request_latency",
    "retrieval_latency",
    "llm_latency"
]:

    print(f"\n{col}")

    print(
        "Average:",
        round(df[col].mean(), 3)
    )

    print(
        "Min:",
        round(df[col].min(), 3)
    )

    print(
        "Max:",
        round(df[col].max(), 3)
    )

    print(
        "P50:",
        round(df[col].quantile(0.50), 3)
    )

    print(
        "P95:",
        round(df[col].quantile(0.95), 3)
    )

    print(
        "P99:",
        round(df[col].quantile(0.99), 3)
    )