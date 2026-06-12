from backend.app.auth.jwt_handler import (
    create_token,
    get_current_user
)

token = create_token(
    "deepak"
)

user = get_current_user(
    token
)

print(user)