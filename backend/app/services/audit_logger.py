from datetime import datetime


def log_access(
    username,
    role,
    query,
    status
):

    log_line = (
        f"{datetime.now()} | "
        f"{username} | "
        f"{role} | "
        f"{status} | "
        f"{query}\n"
    )

    print(
        "[AUDIT]",
        log_line
    )

    with open(
        "audit.log",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            log_line
        )