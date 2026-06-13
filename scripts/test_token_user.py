from backend.app.auth.jwt_handler import (
    get_current_user
)

token = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmaW5hbmNlX3VzZXIifQ.ZDfi-Yrb_sQH-f91HDh6KA_Ho40my5cupY-WLGe0Byc"
)

user = get_current_user(
    token
)

print(user)