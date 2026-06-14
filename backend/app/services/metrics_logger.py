from datetime import datetime

def save_metric(
    name,
    value
):

    with open(
        "metrics.log",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"{datetime.now()},"
            f"{name},"
            f"{value}\n"
        )