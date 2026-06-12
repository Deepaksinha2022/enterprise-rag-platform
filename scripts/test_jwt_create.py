from backend.app.auth.jwt_handler import (
    create_token
)

token = create_token(
    "deepak"
)

print(token)