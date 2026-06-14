from backend.app.services.metrics_logger import (
    save_metric
)

import time

def start_timer():

    return time.time()

def end_timer(
    start_time
):

    return round(
        time.time() - start_time,
        3
    )

def log_metric(
    name,
    value
):

    print(
        f"[METRIC] "
        f"{name}: "
        f"{value}"
    )
    
    save_metric(
        name,
        value
    )

def estimate_tokens(
    text
):

    return len(
        text.split()
    )

def estimate_cost(
    input_tokens,
    output_tokens,
    cost_per_1k_tokens=0.002
):

    total_tokens = (
        input_tokens
        + output_tokens
    )

    cost = (
        total_tokens / 1000
    ) * cost_per_1k_tokens

    return round(
        cost,
        6
    )