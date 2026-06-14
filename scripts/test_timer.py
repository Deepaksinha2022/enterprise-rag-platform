import time

from backend.app.services.observability import (
    start_timer,
    end_timer
)

start = start_timer()

time.sleep(2)

duration = end_timer(
    start
)

print(
    "Duration:",
    duration
)