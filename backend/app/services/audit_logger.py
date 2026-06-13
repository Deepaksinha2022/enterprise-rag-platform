from datetime import datetime


def log_access(
    username,
    role,
    query,
    access_status
):

    timestamp = datetime.now()

    print(

        f"[AUDIT] "

        f"{timestamp} | "

        f"{username} | "

        f"{role} | "

        f"{access_status}"

        f"{query}"
    )