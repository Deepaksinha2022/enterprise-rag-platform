from backend.app.auth.jwt_handler import (
    create_token,
    verify_token
)

token = create_token(
    "deepak"
)

payload = verify_token(
    token
)

print(payload)